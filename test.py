


def calculator(a, b):
    return calcinternals(a, b)


class calcinternals():
    def __init__(self, a, b):
        self.A = a
        self.B = b

    @property
    def sum(self):
        return self.A + self.B

    @property
    def difference(self):
        return self.A - self.B

    @property
    def product(self):
        return self.A * self.B

    @property
    def fraction(self):
        return self.A / self.B


calc = calculator(3,4)

calc.difference
