#coding=utf-8﻿
from typing import List
def multiply_elements(elements: List[int], multiplier: int = 2) -> List[int]:
    return [element * multiplier for element in elements]
elements_input = input("Введите числа: ")
elements = [int(x) for x in elements_input.split()]
multiplier_input = int(input("Введите множитель: ") or "2")
result = multiply_elements(elements, multiplier_input)
print(result)

#Лямбда функция:

﻿multilambda = lambda elements, multiplier=2: [element * multiplier for element in elements]
elements_input = input("Введите числа: ")
elements = [int(x) for x in elements_input.split()]

multiplier_input = int(input("Введите множитель: ") or "2")

result_lambda = multilambda(elements, multiplier_input)
print(result_lambda)