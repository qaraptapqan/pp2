import os


path = input()

if not os.path.exists(path):
    print('Path does not exists')
    exit()
path = os.path.abspath(path)

if os.path.isdir(path):
    print(f'dir portion: {path}')
else: 
    print(f'dir portion: {os.path.dirname(path)}\nfile portion: {os.path.basename(path)}')
