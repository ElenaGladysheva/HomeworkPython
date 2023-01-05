# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
def WeekDay():
    day = int(input("Input number of day in week: "))
    if day in range(1,6):
        print ("No")
    elif day in range(6,8):
        print ("Yes")
    else:
        print("Incorrent input")    
WeekDay()

