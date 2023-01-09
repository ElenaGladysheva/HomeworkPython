# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def MuultiplicationPairNumber (length, end_number):
    input_list = sample (range(1, end_number+1), k=length)
    print(input_list)
    new_list = []
    
    if length % 2:
        for i in range(0, length//2):
            mult = input_list[i] * input_list[(length - 1 - i)] 
            new_list.append(mult) 
        new_list.append(input_list[length//2])
    else:
        for i in range(0, length//2):
            mult = input_list[i] * input_list[(length - 1 - i)] 
            new_list.append(mult) 
    print(new_list)

MuultiplicationPairNumber(int(input("Введите длину списка: ")), int(input("Введите максимальное число в списке: ")))
