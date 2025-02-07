import re


with open('row.txt', 'r') as f:
    pat = r'([A-Z])'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, r' \1', word))
