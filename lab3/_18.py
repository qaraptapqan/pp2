from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'Coordinates are: ({self.x};{self.y})')
    def move(self, m_x, m_y):
        self.x += m_x
        self.y += m_y
        return 1
    def dist(self, point):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)


a = Point(3,4)
a.show()
a.move(7,-6)
a.show()
b = Point(13,2)
b.show()
print(a.dist(b))
