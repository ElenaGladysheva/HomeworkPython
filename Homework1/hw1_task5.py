# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt


def DistancePoint2D ():
    xa = int(input("Input xa: "))
    ya = int(input("Input ya: "))
    xb = int(input("Input xa: "))
    yb = int(input("Input ya: "))
    distance = sqrt((xb - xa)**2 + (yb - ya)**2)
    print(round(distance,2))
DistancePoint2D ()


