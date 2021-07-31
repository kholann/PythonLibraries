# Задание 3
# Найдите скалярное произведение столбцов массива a_centered.
# В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np

a = np.array([[1,2,3,3,1],
             [6,8,11,10,7]]).T

mean_a = np.mean(a, axis=0)

a_centered = a - mean_a

a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])

a_cov = a_centered_sp / (len(a) - 1)

print(f'a_centered_sp = {a_centered_sp}')

print(f'a_cov = {a_cov}')

# a_centered_sp = 8.0
# a_cov = 2.0

