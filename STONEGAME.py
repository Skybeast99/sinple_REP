import os
import random 
enemy_hp = 100
enemy_strength = 100
game = False
player_name = input('введите ваше имя: ')
player_hp = 250
player_strength = 100
player_money = 15
player_ex = 1
player_level = 1


def start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    player_name = input('введите ваше имя: ')
    player_hp = 250
    player_strength = 100
    player_money = 15
    player_ex = 1
    player_level = 1
    visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    os.system('cls')
    show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength) 
    print(player_name, 'приехал к камню')
    print('1 - поехать на арену')
    print('2 - отправиться в таверну')
    print('3 - заглянуть в лавку')
    print('0 - выйти из игры')
    option = input('введите номер варианта ')
    if option == '1':
        visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, enemy_hp) 
    elif option == '2':
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif option == '3':
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, )
    elif option == '0':
        print('вышел из игры')
    else:
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    print('ваше здоровье: ', player_hp)
    print('ваша сила: ', player_strength)
    print('ваши деньги: ', player_money)
    print('ваш опыт: ', player_ex)
    print('ваш левл: ', player_level)


def visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, enemy_hp):
    battle = input("вы хотите поучавствовать в сражении за деньги? (да/нет) ")
    if battle == 'да':
        while player_hp > 0 and enemy_hp > 0:

            your_attack = random.randint(1, player_strength)
            enemy_attack = random.randint(1, enemy_strength)
            print(your_attack)
            print(enemy_attack)
            player_hp -= enemy_attack
            enemy_hp -= your_attack
            print(player_hp)
            print(enemy_hp)
    elif battle =='нет':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:  
        visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, enemy_hp)


def visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    casino = input('вы хотите поиграть в кости на деньги (да/нет) ')
    if casino == 'да':
        bot = random.randint(2, 12)
        num = random.randint(2, 12)
        print('ваши деньги:', player_money)
        bet = int(input('введите вашу ставку: '))
        if player_money >= 1:
            print("ваше число", num)
            print("число бота", bot)
            if num > bot:
                player_money += bet
                print('вы выиграли')
                print('ваши деньги:', player_money)  
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)  
            elif num < bot:
                player_money -= bet  
                print('вы проиграли')
                print('ваши деньги:', player_money)   
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)    
            else:    
                print('ничья')
                print('ваши деньги:', player_money)
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)
        else:
            print('у вас недостаточно денег')
            visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)       
    elif casino == 'нет':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    print('1 - купить зелье здоровья (10 монет)')
    print('2 - купить зелье силы (10 монет)')
    print('3 - купить зелье опыта (15 монет)')
    print('0 - выйти')
    shopping = int(input('что бы вы хотели купить? '))
    if shopping == '1':
        player_hp += 25
        player_money -= 10 
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif shopping == '2':
        player_strength += 10
        player_money -= 10 
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif shopping == '3':
        player_ex += 10
        player_money -= 15
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)

start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength)    
