from timeit import timeit
from task2 import func_1
from task2 import func_2

print(timeit("func_1(333, 2)", globals=globals(), number=100000))
print(timeit("func_2(333, 2)", globals=globals(), number=100000))

'''Всегда разные результаты. В основном ускорения не наблюдается'''


# вариант без импортирования функции
# print(timeit("func_1(x, y)", setup="from task2 import func_1, x, y", number=100000))
# print(timeit("func_2(x, y)", setup="from task2 import func_2, x, y", number=100000))

