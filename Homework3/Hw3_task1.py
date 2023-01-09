# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample
def SumNum (length, end_number):
    new_list = sample (range(1, end_number+1), k=length)
    print(new_list)
    sum = 0
    i = 0
    while i <= length:
        sum += new_list[i]
        i += 2
    return sum
print(SumNum(int(input("Введите длину списка: ")), int(input("Введите максимальное число в списке: "))))

