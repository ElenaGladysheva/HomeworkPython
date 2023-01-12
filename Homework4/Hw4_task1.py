# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

def Accuracy():
    from decimal import Decimal, ROUND_HALF_UP
    number = Decimal(input("Input the your number: "))
    print(number.quantize(Decimal(input("Input the required accuracy: ")), ROUND_HALF_UP))

Accuracy()

