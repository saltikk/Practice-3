class shape:
    def area(self):
        return 0


class square(shape):
    def __init__(self, n):
        self.length = n

    def area(self):
        return self.length * self.length


n = int(input())

sqr = square(n)
print(sqr.area())
