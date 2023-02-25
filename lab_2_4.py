# Маркина Ксения, Прохоренко Юлия, ФБИ-01
# Лабораторная работа №2
# 25.02.2023
# Задание 2.4. Работа со строками в Python.
print('Введите произвольную строку: ')
text = str(input())
j = 0
for i in text:
    if i == 'а':
        text = text.replace(i, 'о')
        j+=1
print(f'Замен: {j}')
print(f'Символов: {len(text)}')
print (text)