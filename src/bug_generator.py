import pickle

file = open('data/guava_code.txt')
file = file.readlines()

# Reformat data
lines = []
for line in file:
    if len(line.split()) > 0:
        lines.append(line.split())

# Search for method calls with 2 arguments and swap them
clean = []
buggy = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if j + 4 >= len(lines[i]):
            break
        if lines[i][j] == '_OParen_' and lines[i][j+2] == '_Com_' and lines[i][j+4] == '_CParen_':
            clean.append(list(lines[i]))
            temp = list(lines[i])
            temp1 = temp[j+1]
            temp[j+1] = lines[i][j+3]
            temp[j+3] = temp1
            buggy.append(temp)

# Save files
with open('clean.pkl', 'wb') as f:
    pickle.dump(clean, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('buggy.pkl', 'wb') as f:
    pickle.dump(buggy, f, protocol=pickle.HIGHEST_PROTOCOL)

