# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, 
# сделать замеры времени, оптимизировать, 
# вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться
# Описания нужно делать в виде docstrings
 
 
'''Поиск самой большой цифры в числе''' 


'''Изначальное решение через цикл'''
def func_1(num):
    max_digit = 0
    while num != 0:
        temp = num % 10
        if temp > max_digit:
            max_digit = temp
        num = num // 10
    return max_digit
print(func_1(23456785432))


'''Оптимизируем через использование встроенной функции max'''
def func_2(num):
    max_digit = 0
    while num:
        temp = num % 10
        max_digit = max(max_digit, temp)
        num = num // 10
    return max_digit
print(func_2(23456785432))
