#coding=utf-8
dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
kluchi=dct.keys()
znach=dct.values()
mnzh1 = set(kluchi)
print("Множество ключей словаря:",mnzh1)
mnzh2 = set(znach)
print("Множество значений словаря:",mnzh2)
mnzh = mnzh1 | mnzh2
print("Объединенное множество:",mnzh)
