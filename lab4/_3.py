from math import tan, pi
a = float(input("Input number of sides: "))
b = float(input("Input the length of a side: "))
print(f'The area of the polygon is: {a * b**2 / 4 / tan(pi/a): .1f}')
