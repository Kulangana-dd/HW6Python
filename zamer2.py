from timeit import timeit

print(timeit("func_1(x, y)", setup="from task2 import func_1, x, y", number=100000))
print(timeit("func_2(x, y)", setup="from task2 import func_2, x, y", number=100000))

'''Не добились ускорения процесса решения'''