import os
path = input()

if not os.path.exists(path):
    raise ValueError('No path like this')

if os.access(path, os.W_OK) and os.access(os.path.dirname(path), os.W_OK):
    os.remove(path)
    print('File deleted')
else: raise PermissionError('Not permitted to delete file')
