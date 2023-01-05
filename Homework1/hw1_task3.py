# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def FindQuarter():
    x = int(input("Input x: "))
    y = int(input("Input y: "))
    if x == 0:
        print("The point on the x-axis.")
    elif y == 0:
        print("The point on the y-axis.")
    elif x > 0 and y > 0:
        print("The point in 1 quarter.")
    elif x < 0 and y > 0:
        print("The point in 2 quarter.")
    elif x < 0 and y < 0:
        print("The point in 3 quarter.")
    else:
        print("The point in 4 quarter.")

FindQuarter()
        
