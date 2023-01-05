# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
num = float(input("Input your number: "))
sum_digits = 0
while num != round(num):
    num *= 10
while not num == 0:
    sum_digits += num % 10
    num //= 10
print(int(sum_digits))
