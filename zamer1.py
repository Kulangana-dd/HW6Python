from timeit import timeit

print(timeit("func_1(23456785432)", setup="from task1 import func_1", number=100000))
print(timeit("func_2(23456785432)", setup="from task1 import func_2", number=100000))

'''Всегда разные результаты. В основном ускорения не наблюдается.'''


# Почему-то не работает через globals

print(timeit("func_1(23456785432)", globals=globals(), number=100000))
print(timeit("func_2(23456785432)", globals=globals(), number=100000))