#coding=utf-8
stepen = [x**2 for x in range(1, 11)]
print(stepen)
﻿
den = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
den_slov = {day: index + 1 for index, day in enumerate(den)}
print(den_slov)

mnozh = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
mnozh_niz = {tag.lower() for tag in mnozh}
print(mnozh_niz)