class Shape:
    def __init__(self, *args):
        self.sides = args
    def area(self):
        if not self.sides:
            return 0
        a = 1
        for _ in self.sides:
            a*=_
        return a

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.length = self.sides[0]
    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = self.sides[0]
        self.width = self.sides[1]
    def area(self):
        return super().area()



q = Square(4)
t = Shape(1,2,3,4,5,6,7)
z = Shape()
g = Rectangle(3,2)
print(q.area())
print(t.area())
print(z.area())
print(g.area())
