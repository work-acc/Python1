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

    def __init__(self, year=1, month=1, day=1):

        try:
            if int(year) and int(month) and int(day):
                self.year = int(year)
                self.month = int(month)
                self.day = int(day)
        except ValueError:
            print('Вы ввели не число!')

    def read(self):
        year = input("Введите год: ")
        month = input("Введите месяц: ")
        day = input("Введите день: ")

        try:
            if int(year) and int(month) and int(day):
                self.year = int(year)
                self.month = int(month)
                self.day = int(day)
        except ValueError:
            print('Вы ввели не число!')

    def display(self):
        print(f"{self.year, self.month, self.day}")

    def add(self, days=10):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days)
        return a + b

    def sub(self, days=10):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days)
        return a - b

    def leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False

    def lt(self, other):
        if isinstance(other, Date):
            a = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=10)
            b = datetime.date(other.year, other.month, other.day) - datetime.timedelta(days=10)
            return a < b
        else:
            raise ValueError()

    def eq(self, other):
        if isinstance(other, Date):
            a = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=10)
            b = datetime.date(other.year, other.month, other.day) - datetime.timedelta(days=10)
            return a == b
        else:
            raise ValueError()

    def gt(self, other):
        if isinstance(other, Date):
            a = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=10)
            b = datetime.date(other.year, other.month, other.day) - datetime.timedelta(days=10)
            return a > b
        else:
            raise ValueError()

    def difference(self, other, days=10):
        if isinstance(other, Date):
            a = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days)
            b = datetime.date(other.year, other.month, other.day) - datetime.timedelta(days)
            return int((a - b).days)
        else:
            raise ValueError()


if __name__ == '__main__':
    r1 = Date()
    r1.read()
    r1.display()
    print(r1.add())
    print(r1.sub())
    print(f'Високосный? {r1.leap_year()}')
    print(f'После: {r1.lt(r1)}')
    print(f'Равно: {r1.eq(r1)}')
    print(f'До: {r1.gt(r1)}')
    print(f'Кол-во дней между датами: {r1.difference(r1)}')
