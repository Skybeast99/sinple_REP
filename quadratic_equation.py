import math
a = int(input("введите a "))
b = int(input("введите b "))
c = int(input("введите c "))
first = b * b
second = 4 * a * c
A = a * 2
d = first - second
D = math.sqrt(d)
x1 = b * -1 + D / A
x2 = b * -1 - D / A
print(x1)
print(x2)