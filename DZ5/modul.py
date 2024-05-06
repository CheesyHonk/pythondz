#coding=utf-8
import math
import statistics
def square_krug():
    print("Введите радиус круга:")
    r = int(input())
    s = math.pi * math.pow(r, 2)
    print("Площадь круга:", s)
def sredniy():
    print("Введите список оценок через пробел:")
    spisok = input()
    spisok2 = spisok.split()
    for i in range(len(spisok2)):
        spisok2[i] = int(spisok2[i])
    srednee = statistics.mean(spisok2)
    print("Средняя оценка:", srednee)
def sberbank():
    price = 317.20
    print("Введите доступные средства:")
    sredstva = int(input())
    akciya = sredstva // price
    print("Вы можете приобрести", akciya, "акций")
    
