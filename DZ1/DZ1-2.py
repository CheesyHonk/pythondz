#coding=utf-8
while True:
     chislo1 = input("Введите число:")
     try:
          chislo2 = int(chislo1)
          print("Числа в интервале [-{},{}]:".format(chislo2,chislo2 + 1))
          minus = 0
          plus = 0
          for i in range(-chislo2,chislo2 + 1):
              print(i, end="")
              if i < 0:
                  minus += i
              elif i > 0:
                  plus += i
          print("Сумма положительных чисел:",plus)
          print("Сумма отрицательных чисел:",minus)
     except ValueError:
         print("Введено не число")
          