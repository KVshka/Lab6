#Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания. 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.

#Вариант 24

#Часть 2

#В первой строке  матрицы должно быть чётное количество нулей. 
#Периметр квадрата, составленного из главных и побочных диагоналей подматриц результирующей матрицы,
#должен содержать максимальное число нулей (за исключением нулевой матрицы)

import matplotlib.pyplot as mpl #Импорт библиотек
import numpy as np
import re

# Тестовые данные
N_test = 10
A_test = np.ones((N_test, N_test), dtype=int)

print('Использовать тестовые данные или случайные?')
while True:
    choice = input('Введите 1, если хотите использовать тестовые данные, 2 - если случайные, q - для выхода из программы): ')
    if choice == '1' or choice == '2' or choice == 'q':
        break

if choice == '1':
    N = N_test
    A = A_test

if choice == '2': # Генерация случайных данных
    while True:
        N = int(input("Введите число N="))
        if N < 2:
            print('Число N слишком малое. Введите N >= 2')
        elif N % 2 != 0:
            print('Введите чётное число N')
        else:
            break
#Формируем матрицу А
    A = np.random.randint(-10, 10, size=(N, N))

if choice == 'q':
    exit()

n = N // 2  # Размерность матриц B, C, D, E (n x n)
Zero = np.zeros((n, n), dtype=int)
B = A[:n,:n]
C = A[:n,n::]
D = A[n::,n::]
E = A[n::,:n]

def F(x, Z):
    if x == 0:
        return Zero
    else:
        return np.copy(Z)


#заменяем подматрицы нулевыми матрицами
max = -1

for a in range(2):
    B_copy = F(a, B)
    for b in range(2):
        C_copy = F(b, C)
        #Ограничение: первая строка матрицы должна содержать чётное количество нулей
        if (len(re.findall(r'\D[0]', str(B_copy[:1,:n]))) + len(re.findall(r'\D[0]', str(C_copy[:1,:n])))) % 2 == 0:
            for c in range(2):
                E_copy = F(c, E)
                for d in range(2):
                    D_copy = F(d, D)
                    Matrix = np.vstack((np.hstack((B_copy, C_copy)), np.hstack((E_copy, D_copy))))
                    if len(re.findall(r'\D[0]', str(Matrix[:N,:N]))) != N*N:
                        #Периметр квадрата, составленного из главных и побочных диагоналей подматриц результирующей матрицы, должен содержать максимальное число нулей
                        sum = len(re.findall(r'\D[0]', str(np.diag(np.flip(B_copy, axis = 1))))) + len(re.findall(r'\D[0]', str(np.diag(C_copy)))) + len(re.findall(r'\D[0]', str(np.diag(np.flip(D_copy, axis = 1))))) + len(re.findall(r'\D[0]', str(np.diag(E_copy))))
                        if max < sum:
                            max = sum
                            Result = np.copy(Matrix)

print('\nРезультирующая матрица:\n', Result)
