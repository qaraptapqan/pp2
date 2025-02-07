from functools import reduce

l = list(map(int, input().split()))

print(reduce(lambda x, y: x*y, l))
