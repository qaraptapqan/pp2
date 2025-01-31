def solve(h, l):
    print(f"Rabbits: {int(l/2) - h}, chickens: {2*h-int(l/2)}")


heads, legs = map(int, input().split())
solve(heads, legs)
