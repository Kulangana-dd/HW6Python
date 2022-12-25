# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, 
# сделать замеры памяти, оптимизировать, вновь выполнить замеры 
# и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

from memory_profiler import profile

'''Поиск самой большой цифры в числе''' 

'''Решение через цикл'''
@profile
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
@profile
def func_2(num):
    max_digit = 0
    while num:
        temp = num % 10
        max_digit = max(max_digit, temp)
        num = num // 10
    return max_digit
print(func_2(23456785432))


'''
Затраты памяти в 1 решении - иногда 25.9 MiB, иногда 25.8 MiB.
Затраты памяти во 2 решении - иногда 25.9 MiB, иногда 25.8 MiB.
В 1 решении - 52 события.
Во 2 решении - 48 событий.
'''