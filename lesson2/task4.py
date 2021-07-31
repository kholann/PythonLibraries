# Задание 4**
# Число, которое мы получили в конце задания 3 является ковариацией двух признаков,
# содержащихся в массиве “а”. В задании 4 мы делили сумму произведений центрированных признаков на N-1,
# а не на N, поэтому полученная нами величина является несмещенной оценкой ковариации.
# В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov.
# В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”.
# В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу
# в строке с индексом 0 и столбце с индексом 1.

import numpy as np

a = np.array([[1,2,3,3,1],
             [6,8,11,10,7]]).T

a_np_cov = np.cov(a.T)

print(f'a_np_cov = {a_np_cov}')
print(f'a_cov = {a_np_cov[0, 1]}')

# a_np_cov = [[1.  2. ]
#  [2.  4.3]]
# a_cov = 2.0