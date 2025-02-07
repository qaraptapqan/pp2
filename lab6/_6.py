for _ in range(ord('A'), ord('Z') +1):
    open(f'assets/{chr(_)}.txt', 'w').close()
