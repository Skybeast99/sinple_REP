from random import*
game = False
money = 10

casino = input("вы хотите поиграть в кости? (да/нет) ")
if casino == "нет":
    print("как скажите")
elif casino == "да":

    while game == False:
        bot = randint(2, 12)
        num = randint(2, 12)
        
        print("у вас", money, "монет")
        player_1 = int(input("сколько вы поставите денег? "))
        
        if player_1 <= money:
            print("ваше число", num)
            print("число бота", bot)
            if num > bot:
                print("вы выиграли", player_1, "монет")
                money += player_1
            elif num < bot:
                money -= player_1
                print("вы проиграли", player_1, "монет")
            else:
                print("ничья")
                
        elif player_1 > money:
            print("у вас нет такой суммы")
            break
        else:
            print("вы ошиблись")
else:
    print("у вас опечатка")

