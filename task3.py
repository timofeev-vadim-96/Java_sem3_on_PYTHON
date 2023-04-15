# Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее из этого списка.

import math
import statistics
arr = [8, 17, 28, 17, 47, 31, 46, 41, 44, 50]
print(f'Исходный массив: \n{arr}\n')
print(f"Минимум: {min(arr)}, максимум: {max(arr)}, медиана: {statistics.median(arr)} \n")
print(f'Отсортированный массив: \n{sorted(arr)}\n')

def find_median_from_arr(input_arr):
    if(len(input_arr)%2!=0): return math.ceil(sorted(input_arr)[int(len(input_arr)/2)])
    else:
        return arr[int((len(arr)/2))]
print(f'Среднее(медианное) значение из списка: {find_median_from_arr(arr)}')



