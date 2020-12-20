#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 14. Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа Pi в данной
# степени.

import math


class Number:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
        self.r = 0
        self.u = 0

        self.difference()
        self.multiplication()

    def read(self):
        x = input("Введите первое число: ")
        y = input("Введите второе число: ")

        self.x = float(x)
        self.y = float(y)

        self.difference()
        self.multiplication()

    def display(self):
        print(f"Разность: {self.r}")
        print(f"Умножение: {self.u}")

    def difference(self):
        if self.x > self.y:
            self.r = self.x - self.y
        else:
            self.r = self.y - self.x

    def multiplication(self):
        self.u = self.x * self.y


class Real(Number):
    def __init__(self, a=1, n=1):
        super(Real, self).__init__()
        self.a = float(a)
        self.n = float(n)
        self.s = 0
        self.p = 0

        self.degree()
        self.pi()

    def read(self):
        a = input("Введите число: ")
        n = input("Введите степень: ")

        self.a = float(a)
        self.n = float(n)

        self.degree()
        self.pi()

    def display(self):
        print(f"Корень числа в произвольной степени: {self.s}")
        print(f"Число Pi в произвольной степени: {self.p}")

    def degree(self):
        self.s = pow(self.n, (1 / self.a))

    def pi(self):
        self.p = math.pi ** self.n


if __name__ == '__main__':
    r1 = Number()
    r1.read()
    r1.display()

    r2 = Real()
    r2.read()
    r2.display()
