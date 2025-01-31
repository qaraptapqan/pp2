def squares(a,b):
    for _ in range(a,b+1):
        yield _*_
a,b = map(int, input("Enter a and b: ").split())
for _ in squares(a,b):
    print(_, end=' ')
