#coding=utf-8
while True:
    print("Введите строку:")
    stroka = input()
    stroka = str.lower(stroka)
    stroka = stroka.replace(' ','')
    print(stroka)
    dct = {}
    for letter in stroka:
        bukva = letter
        chislo = stroka.count(letter)
        dct[letter] = chislo
    print("Символы и их количество:",dct)