def ll(n):
    for _ in range(n, -1, -1):
        yield _
for _ in ll(5):
    print(_, end=' ')
