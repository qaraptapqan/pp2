import re


with open('row.txt', 'r') as f:
    pat = r'(\w)([A-Z]\w+)'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, r'\1 \2', word))

