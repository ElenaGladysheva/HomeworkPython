# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

def Select():
    input_num = (input("Input string of numbers: ")) # Зашла строка

    list_input = input_num.split() # преобразовали в список

    select_list = []

    for i in list_input:
        if i not in select_list:
            select_list.append(i)

    for i in select_list:
        print("".join(str(i)), end=" ") # преобразовали назад в строку с пробелом

