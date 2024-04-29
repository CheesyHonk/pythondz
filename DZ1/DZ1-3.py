#coding=utf-8
def proverka(chislo):
    chislo_str = str(chislo)
    if len(chislo_str) != 3:
        print("Длина числа не равна 3")
        return False
    if len(set(chislo_str)) < len(chislo_str):
           print("В числе есть повторяющиеся цифры")
           return False
    return True
def perestanovka(chislo):
    if not proverka(chislo):
         return
    chislo_str = str(chislo)
    perestanovki = []
    for i in range(3):
        for j in range(3):
             for k in range(3):
                 if i != j and j != k and k !=i:
                      test = int(chislo_str[i] + chislo_str[j] + chislo_str[k])
                      perestanovki.append(test)
    print("Варианты перестановки числа:",perestanovki)
while True:
     chislo = input("Введите трехзначное число:")
     perestanovka(chislo)
           