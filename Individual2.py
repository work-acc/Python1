# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа PI в данной
# степени.

import math


class Number:
    def __init__(self, num=0):
        self.num = float(num)

    def mul(self, other):
        return Number(self.num * other.num)

    def sub(self, other):
        return Number(self.num - other.num)


class Real(Number):
    def __init__(self, num=0):
        super(Real, self).__init__(num)

    def sqrtn(self, n):
        return self.num ** (1 / n)

    def pow(self, other):
        return math.pi ** other.num


if __name__ == '__main__':
    r1 = Number(2)
    r2 = Real(4)
    r = r1.mul(r2)
    print(r.num)
    r = r1.sub(r2)
    print(r.num)
    r = r2.sqrtn(2)
    print(r)
    r = r2.pow(r1)
    print(r)
