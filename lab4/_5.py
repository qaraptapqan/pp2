def square(n):
    for _ in range(1, n+1):
        yield _*_

for i in square(5):
    print(i, end=' ')
