import numpy as np

# Создание массива
arr = np.array([1, 2, 3, 4, 5])

# Математические операции
print(f"Сумма элементов массива: {np.sum(arr)}")
print(f"Среднее значение массива: {np.mean(arr)}")
print(f"Стандартное отклонение массива: {np.std(arr)}")

# Вывод массива
print(f"Массив: {arr}")

# Создание многомерного массива
matrix = np.array([[1, 2], [3, 4]])

# Математические операции с матрицей
print(f"Транспонированная матрица: \n{matrix.T}")
print(f"Определитель матрицы: {np.linalg.det(matrix)}")
print(f"Обратная матрица: \n{np.linalg.inv(matrix)}")

