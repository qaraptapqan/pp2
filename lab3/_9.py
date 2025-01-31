from math import pi as meow
def solve(r):
    return (4 / 3) * meow * r ** 3
r = float(input())
print(f'Radius ={solve(r): .2f}')
