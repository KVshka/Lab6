#Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания. 
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.

#Вариант 24

#Часть 1

#Дана квадратная матрица, состоящая из четырех равных по размерам подматриц. 
#Сформировать все возможные варианты данной матрицы путем последовательной замены подматриц нулевыми подматрицами.

import matplotlib.pyplot as mpl #Импорт библиотек
import numpy as np

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

#n_first = n
#if N % 2 == 0:
#    n_second = n
#else:
#    n_second = n+1

#B = A[:n_second,:n_second]
#C = A[:n_second,n_first::]
#D = A[n_first::,n_first::]
#E = A[n_first::,:n_second]

# Печатаем матрицы A, E, B, C, D
print('\nМатрица A:\n', A)
print('\nМатрица B:\n', B)
print('\nМатрица C:\n', C)
print('\nМатрица D:\n', D)
print('\nМатрица E:\n', E)

print('\nРезультирующие матрицы:')

def F(x, Z):
    if x == 0:
        return Zero
    else:
        return np.copy(Z)

#заменяем подматрицы нулевыми матрицами
for a in range(2):
    B_copy = F(a, B)
    for b in range(2):
        C_copy = F(b, C)
        for c in range(2):
            E_copy = F(c, E)
            for d in range(2):
                D_copy = F(d, D)
                Result = np.vstack((np.hstack((B_copy, C_copy)), np.hstack((E_copy, D_copy))))
                print('\n', Result)