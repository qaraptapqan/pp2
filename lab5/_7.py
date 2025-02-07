import re


with open('row.txt', 'r') as f:
    pat = r'_([a-z])'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, lambda x: x.group(1).upper(), word))
