from timeit import timeit
from task1 import func_1
from task1 import func_2

print(timeit("func_1(23456785432)", globals=globals(), number=100000))
print(timeit("func_2(23456785432)", globals=globals(), number=100000))

'''Всегда разные результаты. В основном ускорения не наблюдается'''

# вариант без импортирования функции
#print(timeit("func_1(23456785432)", setup="from task1 import func_1", number=100000))
#print(timeit("func_2(23456785432)", setup="from task1 import func_2", number=100000))