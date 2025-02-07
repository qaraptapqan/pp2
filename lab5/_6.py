import re


with open('row.txt', 'r') as f:
    pat = r'[ ,.]'
    l = f.read().split()

    for word in l:
        print(re.sub(pat, ':', word))
