import re


with open('row.txt', 'r') as f:
    pat = r'[A-Z][a-z]+'
    l = f.read().split()

    for word in l:
        if re.fullmatch(pat, word):
            print(word)

