import re

with open('row.txt', 'r') as f:
    pat = r'ab{2,3}'
    l = f.read().split()

    for word in l:
        if re.fullmatch(pat, word):
            print(word)
