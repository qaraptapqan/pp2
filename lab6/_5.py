s = input().split()
with open('assets/asset.txt', 'w') as f:
    for _ in s:
        f.write(_+'\n')
        
