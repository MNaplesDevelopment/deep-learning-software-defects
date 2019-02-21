import numpy as np
import os
import json

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

    return codeString.split()

# with open(os.getcwd() + "/jsons/hi7.json") as f:
#     text = json.load(f)
with open(os.getcwd() + "/py2vec/py2vec_model_Java.json") as f:
    embs = json.load(f)

print(embs['getsize'])
print("HOWDY YALL")

lines = []
for i in range(len(text)):
    lines.append(StringTokenizer(text[i]['line']))

lines = np.asarray(lines)

#print(lines[:30])
clean = []
buggy = []
for i in range(lines.shape[0]):
    for j in range(len(lines[i])):
        if j + 4 >= len(lines[i]):
            break
        if lines[i][j] == '_openParen_' and lines[i][j+2] == '_comma_' and lines[i][j+4] == '_closeParen_':
            clean.append(list(lines[i]))
            temp = list(lines[i])
            temp1 = temp[j+1]
            temp[j+1] = lines[i][j+3]
            temp[j+3] = temp1
            buggy.append(temp)
#
# for i in range(len(clean)):
#     print(clean[i])
#     print(buggy[i])

# with open(os.getcwd() + "/py2vec/buggy.json", "w+") as f:
#     json.dump(buggy, f, indent=4)
#
# with open(os.getcwd() + "/py2vec/clean.json", "w+") as f:
#     json.dump(clean, f, indent=4)
