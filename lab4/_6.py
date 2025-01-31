def even(n):
    for _ in range(2, n+1):
        if _%2==0: yield _

n = int(input("Enter limit: "))
print(', '.join(map(str, list(even(n)))))
