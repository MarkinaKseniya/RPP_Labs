# Маркина Ксения, Прохоренко Юлия, ФБИ-01
# Лабораторная работа №2
# 25.02.2023
# Задание 3.4. Работа со списками. Операции над списками в Python.
import sys
arr = []
for massiv in sys.argv[1:]:
    arr.append(int(massiv))
    # print(arr)

tmp_value = 0
tmp_index = 0
for i, v in enumerate(arr):
    if v > tmp_value:
        tmp_value = v
        tmp_index = i

print("Максимальный элемент {}, найден с индексом {}".format(tmp_value, tmp_index))

b = []
for i in range(len(arr) - 1, -1, -1):
    if int(arr[i]) % 2 > 0:
        b.append(arr[i])

if len(b) == 0:
    print("Таких чисел нет!")
else:
    print(b)
