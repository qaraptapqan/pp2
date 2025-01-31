def gh(n):
    for _ in range(n):
        if _%3 == 0 and _%4 == 0:
            yield _
n = int(input("Enter limit: "))

for i in gh(n):
    print(i, end = ' ')
