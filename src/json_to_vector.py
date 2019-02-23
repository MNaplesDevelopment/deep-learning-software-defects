import re
from W2V_trainer import Word2VecTrainer

file = open('data/guava_code.txt')
file = file.read()

# Remove comments
s = re.sub(r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', '', file, re.MULTILINE)

# Tokenize Java Syntax
def string_tokenizer(code_string):
    code_string = code_string.replace("://", ' _URL_ ')
    code_string = code_string.replace(">>>", ' _UnRS_ ')
    code_string = code_string.replace("<<<", ' _UnLS_ ')
    code_string = code_string.replace(">>=", ' _RSA_ ')
    code_string = code_string.replace("<<=", ' _LSA_ ')
    code_string = code_string.replace("\\n", '')
    code_string = code_string.replace(">>", ' _RS_ ')
    code_string = code_string.replace("<<", ' _LS_ ')
    code_string = code_string.replace("==", ' _Eql_ ')
    code_string = code_string.replace("!=", ' _NEql_ ')
    code_string = code_string.replace("++", ' _Inc_ ')
    code_string = code_string.replace("--", ' _Dec_ ')
    code_string = code_string.replace("&&", ' _And_ ')
    code_string = code_string.replace("||", ' _Or_ ')
    code_string = code_string.replace("<=", ' _GTE_ ')
    code_string = code_string.replace(">=", ' _LTE_ ')
    code_string = code_string.replace("+=", ' _PlusA_ ')
    code_string = code_string.replace("-=", ' _MinA_ ')
    code_string = code_string.replace("*=", ' _MultA_ ')
    code_string = code_string.replace("/=", ' _DivA_ ')
    code_string = code_string.replace("%=", ' _ModA_ ')
    code_string = code_string.replace("&=", ' _BAA_ ')
    code_string = code_string.replace("^=", ' _BXA_ ')
    code_string = code_string.replace("|=", ' _BOA_ ')
    code_string = code_string.replace("\\", ' _FS_ ')
    code_string = code_string.replace(",", ' _Com_ ')
    code_string = code_string.replace("?", ' _QM_ ')
    code_string = code_string.replace(".", ' _Dis_ ')
    code_string = code_string.replace("[", ' _OBrac_ ')
    code_string = code_string.replace("]", ' _CBrac_ ')
    code_string = code_string.replace("'", ' _SQ_ ')
    code_string = code_string.replace('"', ' _DQ_ ')
    code_string = code_string.replace("(", ' _OParen_ ')
    code_string = code_string.replace(")", ' _CParen_ ')
    code_string = code_string.replace(":", ' _Colon_ ')
    code_string = code_string.replace(";", ' _SemCol_ ')
    code_string = code_string.replace("+", ' _Plus_ ')
    code_string = code_string.replace("-", ' _Minus_ ')
    code_string = code_string.replace("*", ' _Mult_ ')
    code_string = code_string.replace("/", ' _Div_ ')
    code_string = code_string.replace("%", ' _Mod_ ')
    code_string = code_string.replace("=", ' _Eql_ ')
    code_string = code_string.replace(">", ' _GT_ ')
    code_string = code_string.replace("<", ' _LT_ ')
    code_string = code_string.replace("!", ' _LN_ ')
    code_string = code_string.replace("&", ' _BA_ ')
    code_string = code_string.replace("|", ' _BO_ ')
    code_string = code_string.replace("^", ' _BX_ ')
    code_string = code_string.replace("~", ' _BC_ ')
    code_string = code_string.replace("#", ' _Hash_ ')
    code_string = code_string.replace("@", ' _At_ ')
    code_string = code_string.replace("`", ' _BT_ ')
    code_string = code_string.replace("{", ' _OCB_ ')
    code_string = code_string.replace("}", ' _CCB_ ')
    code_string = code_string.replace("$", ' _Dol_ ')

    return code_string

# Save cleaned and tokenized code
s = string_tokenizer(s)
with open('data/guava_code.txt', 'w') as file:
    file.write(s)

# Run Word2Vec to create embeddings
Word2Vec = Word2VecTrainer(input_file='data/guava_code.txt', output_file='data/embs.vec')
Word2Vec.train()
