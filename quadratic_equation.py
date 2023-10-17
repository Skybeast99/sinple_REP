import math
a = int(input("введите a "))
b = int(input("введите b "))
c = int(input("введите c "))
first = b * b
second = 4 * a * c
A = a * 2
d = first - second
if d >= 1:
    D = math.sqrt(d)
    y1 = b * -1 + D 
    y2 = b * -1 - D
    x1 = y1 / A
    x2 = y2 / A
    print(x1)
    print(x2)
elif d == 0:
    x1 = b * -1 / A
    print(x1)
else:
    print("корней нет")
