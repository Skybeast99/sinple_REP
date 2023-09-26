name = "илья Муромец"

way_1 = False
way_2 = False
way_3 = False

while way_1 == False or way_2 == False or way_3 == False:
    print(name, "~приехал к камню на нем~")
    print("~налево пойдешь убит будешь~") == True
    print("~направо пойдешь богат будешь~") == True
    print("~прямо пойдешь богат будешь~") == True

    way = input("В КАКУЮ СТОРОНУ ЕХАТЬ ")

    if way == "налево":
        if way_1 == False:
            print(name, "убит")
            way_1 = True
        else:
            print("ты уже был на этой дороге")
    elif way == "прямо":
        if way_2 == False:
            print(name, "женат")
            way_2 = True
        else:
            print("ты уже был на этой дороге")
    elif way == "направо":
        if way_3 == False:
            print(name, "богат")
            way_3 = True
        else:
            print("ты уже был на этой дороге")
    else:
        print(name, "нет такой дороги")

print("СКАЗКЕ КОНЕЦ")
