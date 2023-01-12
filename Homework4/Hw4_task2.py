# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def PrimeFactors(num):

    i = 2
    primfac = []
    while num >= i*i:
       while num % i == 0:
           primfac.append(i)
           num = num / i
       i += 1
    if num >= 1:
       primfac.append(round(num))
        
    return sorted(primfac)

num = float(input("Input the integer number: ")) 

if (num <= 0) or (num % 1):
        print("Incorrent number")
else:
    num = int(num)
    print("{} : {}".format(num, PrimeFactors(num)))

