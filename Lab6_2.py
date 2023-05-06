#Импорт библиотек
import numpy as np
import re

# Тестовые данные
N_test = 10
A_test = np.array([[9, 7, 0, 7, 6, 0, 5, 7, 0, 0],
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

B = A[:n_first,:n_first]
C = A[:n_first,n_second::]
D = A[n_second::,n_second::]
E = A[n_second::,:n_first]

# Печатаем матрицы A, E, B, C, D
print('\nМатрица A:\n', A)
print('\nМатрица B:\n', B)
print('\nМатрица C:\n', C)
print('\nМатрица D:\n', D)
print('\nМатрица E:\n', E)

def Null(x):
    if x % 2 != 0:
        if A[0][n_second] == 0:
            return 0
    if len(re.findall(r'\D[0]', str(A[:1,:]))) > 0:
        if len(re.findall(r'\D[0]', str(A[:1,:n_first]))) == 0:
            if len(re.findall(r'\D[0]', str(A[:1,n_first::]))) == n:
                return 3
            else:
                return 1
        elif len(re.findall(r'\D[0]', str(A[:1,n_first::]))) == 0:
            if len(re.findall(r'\D[0]', str(A[:1,:n_first]))) == n:
                return 4
            else:
                return 2
        elif len(re.findall(r'\D[0]', str(A[:1,:]))) == n:
            return 5
        else:
            return 0
    else:
        return 6

max = max(len(re.findall(r'\D[0]', str(np.diag(E)))), len(re.findall(r'\D[0]', str(np.diag(np.flip(D, axis = 1))))))
A_copy = np.copy(A)
if Null(N) == 0:
    print("Данная матрица не удовлетворяет условию")
if Null(N) == 1:
    A_copy[:n_first,n_second::] = 0
if Null(N) == 2:
    A_copy[:n_first,:n_first] = 0
if Null(N) == 3:
    if max > len(re.findall(r'\D[0]', str(np.diag(np.flip(B, axis = 1))))):
        A_copy[:n_first,:n_first] = 0
    elif len(re.findall(r'\D[0]', str(np.diag(E)))) > len(re.findall(r'\D[0]', str(np.diag(np.flip(D, axis = 1))))):
        A_copy[n_second::,n_second::] = 0
    else:
        A_copy[n_second::,:n_first] = 0
if Null(N) == 4:
    if max > len(re.findall(r'\D[0]', str(np.diag(C)))):
        A_copy[:n_first,n_second::] = 0
    elif len(re.findall(r'\D[0]', str(np.diag(E)))) > len(re.findall(r'\D[0]', str(np.diag(np.flip(D, axis = 1))))):
        A_copy[n_second::,n_second::] = 0
    else:
        A_copy[n_second::,:n_first] = 0
if Null(N) == 5:
    if len(re.findall(r'\D[0]', str(np.diag(E)))) > len(re.findall(r'\D[0]', str(np.diag(np.flip(D, axis = 1))))):
        A_copy[n_second::,n_second::] = 0
    else:
        A_copy[n_second::,:n_first] = 0
if Null(N) == 6:
    if len(re.findall(r'\D[0]', str(np.diag(C)))) > len(re.findall(r'\D[0]', str(np.diag(np.flip(B, axis = 1))))):
        A_copy[:n_first,:n_first] = 0
    else:
        A_copy[:n_first,n_second::] = 0

print('\nРезультирующая матрица:\n', A_copy)

