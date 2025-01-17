# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:18:25 2019
По введенным пользователем координатам двух точек вывести уравнение прямой
вида y = kx + b, проходящей через эти точки.

"""
# Ввод
print('Введите координаты двух точек на плоскости (x1, y1) и (x2, y2)')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

# Проверка варианта вертикальной прямой
if x1 == x2:
    print(f'Уравнение прямой: x = {x1}')

# Расчет линейных коэффициентов и вывод резултатов
else:
    k = (y2-y1)/(x2-x1)
    b = y1 - k*x1
    if k == 0:
        print(f'Уравнение прямой: y = {b}')
    elif b == 0:
        print(f'Уравнение прямой: y = {k}*x')
    else:
        print(f'Уравнение прямой: y = {k}*x + {b}')
