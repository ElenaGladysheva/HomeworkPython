# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011
def Binarization (number):
    num = number
    k = 1
    while k < num:
        k *= 2
    k //= 2
    while k >= 1:
        if num >= k:
            print(1, end = "")
            num -= k
        else:
            print(0, end = "")
        k //= 2
    
Binarization (int(input("Введите десятичное число: ")))
