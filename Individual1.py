#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 7. Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
# структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
# включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
# (например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
# через заданное количество дней, вычитание заданного количества дней из даты,
# определение високосности года, присвоение и получение отдельных частей (год, месяц,
# день), сравнение дат (равно, до, после), вычисление количества дней между датами.

import datetime


class Date:

    def __init__(self, year=1, month=1, day=1, number=0):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.number = float(number)

    def read(self):
        year = input("Введите год: ")
        month = input("Введите месяц: ")
        day = input("Введите день: ")
        number = input("Количество дней: ")

        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.number = float(number)

    def display(self):
        print(f"{self.year}")
        print(f"{self.month}")
        print(f"{self.day}")

    def add(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        return a + b

    def sub(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        return a - b

    def leap_year(self):
        leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
        return f"Високосный: {leap}"

    def lt(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        return f"После: {a + b < a - b}"

    def eq(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        return f"Равно: {a + b == a - b}"

    def gt(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        return f"До: {a + b > a - b}"

    def difference(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        x = a + b
        y = a - b
        return x - y


if __name__ == '__main__':
    r1 = Date()
    r1.read()
    r1.display()
    print(r1.add())
    print(r1.sub())
    print(r1.leap_year())
    print(r1.lt())
    print(r1.eq())
    print(r1.gt())
    print(r1.difference())
