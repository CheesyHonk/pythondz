#coding=utf-8
chisla = []
stepen = int(input("Введите степень: "))
kolvo = int(input("Введите кол-во чисел в списке: "))

for i in range(kolvo):
    nomer = input("Введите число, которое нужно возвести в степень: ")
    chisla.append(nomer)


for nomer in chisla:
    if nomer.isdigit() or (nomer.startswith('-') and nomer[1:].isdigit()):  
        nomer = float(nomer)  
        powered_num = nomer ** stepen
        print(f"{nomer} в степени {stepen} = {powered_num}")
    else:
        print(f"{nomer} * {stepen} =", nomer * stepen)  