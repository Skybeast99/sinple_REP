x = int(input("введите абсциссу x "))
y = int(input("введите ординату y "))

if x == 0 and y > 0:
    print("вверху")
elif x == 0 and y < 0:
    print("внизу")
elif x > 0 and y == 0:
    print("впереди")
elif x < 0 and y == 0:
    print("сзади")
elif x < 0 and y < 0: 
    print("левый нижний угол")
elif x > 0 and y > 0:
    print("правый верхний угол")
elif x < 0 and y > 0:
    print("левый верхний угол")
elif x > 0 and y < 0:
    print("правый нижний угол")
else:
    print("центр")

