import matplotlib.pyplot as mpl #Импорт библиотек
import numpy as np

# Тестовые данные
N_test = 10
A_test = np.array([[9, 5, 1, 6, -3, -8, -7, 1, 1, 10],
    [1, 6, -5, -1, -4, -1, 10, 5, -10, -6],
    [-8, -2, -3, 7, 9, 1, 8, 0, 9, 5],
    [-7, 6, 0, -8, 4, 2, 1, -8, -5, -1],
    [-3, -9, -4, -1, -5, -3, -6, 9, 7, -6],
    [-7, 1, 7, 8, -3, 5, 7, -1, -7, -6],
    [-1, 6, -5, 2, 2, 2, 3, 10, -8, 4],
    [-4, -2, 1, -2, -2, -4, -7, -10, 15, 5],
    [2, -3, 0, -7, -1, 0, 9, -8, 9, 4],
    [-8, -10, 3, 0, -5, 10, -8, -10, -1, 8]
    ])

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
        else:
            break
#Формируем матрицу А
    A = np.random.randint(-10, 10, size=(N, N))

if choice == 'q':
    exit()

n = N // 2  # Размерность матриц B, C, D, E (n x n)
n_first = n
if N % 2 == 0:
    n_second = n
else:
    n_second = n+1

B = A[:n_second,:n_second]
C = A[:n_second,n_first::]
D = A[n_first::,n_first::]
E = A[n_first::,:n_second]

# Печатаем матрицы A, E, B, C, D
print('\nМатрица A:\n', A)
print('\nМатрица B:\n', B)
print('\nМатрица C:\n', C)
print('\nМатрица D:\n', D)
print('\nМатрица E:\n', E)

print('\nРезультирующие матрицы:')
i=0
while i <=n_second:
    j=0
    while j <=n_second:
        A_copy = np.copy(A)
        A_copy[i:n_second+i,j:n_second+j] = 0
        print('\n', A_copy)
        j+=n_second
    i+=n_second