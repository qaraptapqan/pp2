def solve(s):
    return True if s == s[::-1] else False

s = input()
print(solve(s))
