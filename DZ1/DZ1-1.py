﻿#coding=utf-8
while True:
    chislo = input("Введите число:")
    if chislo == 'exit':
        print("Выход из программы")
        break
    try:
        number = int(chislo)
        length = len(str(number))
        print("Длина числа:",length)
    except ValueError:
        print("Введено не число")