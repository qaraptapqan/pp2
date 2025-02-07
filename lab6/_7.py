with open('assets/asset.txt', 'r') as f:
    with open('assets/asset2.txt', 'w') as file:
        file.write(f.read())
