def spy_game(a):
    for i in range(len(a) - 2):
        if a[i] == 0:
            if a[i + 1] == 0:
                if a[i + 2] == 7:
                    print(True)
                    return
    print(False)
a = list(map(int, input().split()))
spy_game(a)
