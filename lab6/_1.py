import os


path, mode = input().split()


if os.path.exists(path):
    if mode == '-df' or mode == '-fd':
        for _ in os.listdir(path):
            print(_)
        exit() 


    if mode == '-f':
        print('Files are: ')
        for _ in os.listdir(path):
            if os.path.isfile(os.path.join(path, _)):
                print(_)

    elif mode == '-d':
        print('Dirs are: ')
        for _ in os.listdir(path):
            if os.path.isdir(os.path.join(path, _)):
                print(_)
        
else:
    print('The heck, there is no path like this')
