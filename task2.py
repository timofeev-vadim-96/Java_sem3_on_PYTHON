# Пусть дан произвольный список целых чисел, удалить из него чётные числа
import random
arr = [random.randint(1,51) for x in range(20)]
print(f'Исходный массив: \n{arr}\n')
data = list(filter(lambda x: x%2 != 0, arr))
print(f'Массив без четных чисел: \n{data}')