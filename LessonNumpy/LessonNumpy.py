from cgi import print_form

import numpy as np

# создание простых массивов numpy
numArray = np.array([1, 29, 40, 56])
print(numArray)

numArrayFloat = np.array([2.544, 3.4, 5, 10, 23.4, 8.0])
print(numArrayFloat)

# создание массивов с определенным промежутком числа
numList = list(range(0,21,5))
print(numList)

nArrayRange = np.arange(0, 21, 5)
print(nArrayRange)

# Линейный интервал
c = np.linspace(0, 1, 5) # [0, 0.25, 0.5, 0.75,  1]
c2 = np.linspace(0, 15, 5) # [ 0.  3.75  7.5  11.25  15. ]
print(c)
print(c2)

# Заполнение нулями и единацми матрицы
z = np.zeros((5, 4))   # заполнение только нулями
print(z)

onearrayMatrix = np.ones((5, 4)) # заполнение только единицами
print(onearrayMatrix)

rng = np.random.default_rng(seed=42)
# Получение случайных чисел
randomNumbers = np.random.randn(3,3)
print(randomNumbers)

randomNums2 = np.random.rand(3, 4)
print(randomNums2)

int_nums = rng.integers(low=50, high=100, size=(5, 4))
print(int_nums)


# Создание матрицы
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

# Основные свойства матрицы
# ndim - кол-во измерений
print(matrix.ndim)

# shape - сколько рядов и сколько колонок
print(matrix.shape)

# size - общее кол-во элементов
print(matrix.size)

# dtype - тип данных элементов
print(matrix.dtype)


# Заполнение матрицы только с определенным числом
fullNumSeven_Matrix = np.full((4,5), 7)
print(fullNumSeven_Matrix)

matrix2 = np.array([
    [2, 4, 5, 6],
    [3, 5, 6, 3],
    [5, 6, 8, 2]
])

print(matrix2.shape)

# Математические операции с матрицей

# Добавление к каждому элементу
print(matrix2)
print(matrix2 + 5)
"""
[[ 7  9 10 11]
 [ 8 10 11  8]
 [10 11 13  7]]
"""
# вычитание с каждого элемента
print(matrix2)
print(matrix2 - 5)
""" 
[[-3 -1  0  1]
 [-2  0  1 -2]
 [ 0  1  3 -3]]
"""

# умножение каждого элемента
print(matrix2)
print(matrix2 * 5)
""" 
[[10 20 25 30]
 [15 25 30 15]
 [25 30 40 10]]
"""

# деление каждого элемента
print(matrix2)
print(matrix2 / 2)
""" 
[[1.  2.  2.5 3. ]
 [1.5 2.5 3.  1.5]
 [2.5 3.  4.  1. ]]
"""

# возведение в степень каждого элемента
print(matrix2)
print(matrix2 ** 2)
""" 
[[ 4 16 25 36]
 [ 9 25 36  9]
 [25 36 64  4]]
"""





