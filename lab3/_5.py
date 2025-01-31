from itertools import permutations

def solve(a):
    for _ in permutations(a):
        print(''.join(_))
        
a = input()
solve(a)
