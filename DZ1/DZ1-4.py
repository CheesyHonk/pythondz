#coding=utf-8
def proverka(vistrel, ship):
    vistrel = vistrel.lower()
    ship = ship.lower()
    
    if vistrel in ship:
        return "Попадание"
    else:
        return "Промах"
imya = input("Введите свое имя:")
familiya = input("Введите свою фамилию:")
vozrast = input("Введите свой возраст:")
print("Ваше имя: {test1},ваша фамилия: {test2},ваш возраст: {test3}".format(test1=imya,test2=familiya,test3=vozrast))
while True:
 ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
 vistrel_igroka = input("Введите координаты для выстрела: ")
 result = proverka(vistrel_igroka, ship)
 print(result)