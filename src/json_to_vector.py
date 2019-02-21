from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.mllib.feature import Word2Vec
import _pickle as pickle
import json
import numpy as np
import os


#conf = SparkConf().setAppName("Name01").setMaster(2)


# Initialize Spark Context
sc = SparkContext()
sqlCtx = SQLContext(sc)

# Load the file created by repo_to_json.py that contains the git blame information
# and store it into a Spark RDD.
code_lines = sqlCtx.read.json(os.getcwd() + "\jsons\hi7_spark.json")

# Repartition the dataset
code_lines = code_lines.repartition(300)


# Tokenizes Java source code.
def StringTokenizer(codeString):
    codeString = codeString.replace("://", ' _urlColonBackslashBackslash_ ')
    codeString = codeString.replace(">>>", ' _zeroFillRightShift_ ')
    codeString = codeString.replace(">>=", ' _rightShiftAssignment_ ')
    codeString = codeString.replace("<<=", ' _leftShiftAssignment_ ')
    codeString = codeString.replace("\\n", '')
    codeString = codeString.replace(">>", ' _rightShift_ ')
    codeString = codeString.replace("<<", ' _leftShift_ ')
    codeString = codeString.replace("==", ' _equality_ ')
    codeString = codeString.replace("!=", ' _notEqual_ ')
    codeString = codeString.replace("++", ' _increment_ ')
    codeString = codeString.replace("--", ' _decrement_ ')
    codeString = codeString.replace("&&", ' _and_ ')
    codeString = codeString.replace("||", ' _or_ ')
    codeString = codeString.replace("<=", ' _greaterThanEqualTo_ ')
    codeString = codeString.replace(">=", ' _lessThanEqualTo_ ')
    codeString = codeString.replace("+=", ' _plusAssignment_ ')
    codeString = codeString.replace("-=", ' _minusAssignment_ ')
    codeString = codeString.replace("*=", ' _multiplyAssignment_ ')
    codeString = codeString.replace("/=", ' _divideAssignment_ ')
    codeString = codeString.replace("%=", ' _modulousAssignment_ ')
    codeString = codeString.replace("&=", ' _bitwiseAndAssignment_ ')
    codeString = codeString.replace("^=", ' _bitwiseXorAssignment_ ')
    codeString = codeString.replace("|=", ' _bitwiseOrAssignment_ ')
    codeString = codeString.replace("\\", ' _forwardSlash_ ')
    codeString = codeString.replace(",", ' _comma_ ')
    codeString = codeString.replace("?", ' _questionMark_ ')
    codeString = codeString.replace(".", ' _dispatch_ ')
    codeString = codeString.replace("[", ' _openBracket_ ')
    codeString = codeString.replace("]", ' _closeBracket_ ')
    codeString = codeString.replace("'", ' _singleQuote_ ')
    codeString = codeString.replace('"', ' _doubleQuote_ ')
    codeString = codeString.replace("(", ' _openParen_ ')
    codeString = codeString.replace(")", ' _closeParen_ ')
    codeString = codeString.replace(":", ' _colon_ ')
    codeString = codeString.replace(";", ' _semicolon_ ')
    codeString = codeString.replace("+", ' _plus_ ')
    codeString = codeString.replace("-", ' _minus_ ')
    codeString = codeString.replace("*", ' _multiply_ ')
    codeString = codeString.replace("/", ' _divide_ ')
    codeString = codeString.replace("%", ' _modulous_ ')
    codeString = codeString.replace("=", ' _equal_ ')
    codeString = codeString.replace(">", ' _greaterThan_ ')
    codeString = codeString.replace("<", ' _lessThan_ ')
    codeString = codeString.replace("!", ' _logicalNot_ ')
    codeString = codeString.replace("&", ' _bitwiseAnd_ ')
    codeString = codeString.replace("|", ' _bitwiseOr_ ')
    codeString = codeString.replace("^", ' _bitwiseXor_ ')
    codeString = codeString.replace("~", ' _bitwiseCompliment_ ')
    codeString = codeString.replace("#", ' _hashSymbol_ ')
    codeString = codeString.replace("@", ' _atSignSymbol_ ')
    codeString = codeString.replace("`", ' _backTicks_ ')
    codeString = codeString.replace("{", ' _curlyOpenBracket_ ')
    codeString = codeString.replace("}", ' _curlyCloseBracket_ ')
    codeString = codeString.replace("$", ' _dollarSignSymbol_ ')

    return codeString


# Process the json file by extracting the lines of code, tokenizing
# the code, lower casing it, and filtering out empty lines. This gives us
# a dataset of tokenized source code that is ready to be fed into word2vec.
words = code_lines.rdd\
    .map(
        lambda line: StringTokenizer(line[11]).split()
    )\
    .map(lambda line: [f.lower() for f in line])\
    .filter(lambda line: line != [])


# Initialize Word2Vec object.
word2vec = Word2Vec()

# Set the minimum number of times a word needs to appear in the dataset
# to generate a vector for it. We are using a very low minimum number
# here because we are only currently testing on a small dataset, a larger
# minimum would be preferable when using large datasets.
word2vec.setMinCount(2)    # Default 100

# Set the size of the embeddings.
word2vec.setVectorSize(100)  # Default 100

# Train the Word2Vec model and produce embeddings.
model = word2vec.fit(words)

# Save the words and their embeddings into a dictionary.
model_dict = {k: list(v) for k, v in dict(model.getVectors()).items()}

# Save the embeddings to a json file.
with open(os.getcwd() + "\py2vec\py2vec_modelJ.json", "w+") as f:
    json.dump(model_dict, f, indent=4)

model_dict = {k: np.array(list(v)) for k, v in dict(model.getVectors()).items()}

# Save the embeddings to a pickle file.
with open(os.getcwd() + "\py2vec\py2vec_modelJ.pkl", "wb+") as f:
    pickle.dump(model_dict, f)
