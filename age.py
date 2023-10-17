age = int(input("сколько вам лет"))

if age == 11:
    print("вам 11 лет")
elif age % 10 and age % 100:
    print("вам" ,age, "год")
elif age > 10 and age < 15:
    print("вам" ,age, "лет")
elif age % 10 > 4:
    print("вам" ,age, "лет")
elif age % 10 == 0:
    print("вам", age, "лет")
else:
    print("вам" ,age, "года")
