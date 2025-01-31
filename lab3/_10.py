def solve(a):
    b = []
    for _ in a:
        if _ not in b: b.append(_)
    return b
a = input().split()
print(" ".join(solve(a)))
