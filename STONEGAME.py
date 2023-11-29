import os
import random
player_name = 1 
game = False
player_hp = 250
player_strength = 100
player_money = 10
player_ex = 1
player_level = 1


def start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength,):
    player_name = input('~ВВЕДИТЕ ВАШЕ ИМЯ~: ')
    player_hp = 250
    player_strength = 100
    player_money = 15
    player_ex = 0
    player_level = 1
    visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    os.system('cls')
    show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength) 
    print(player_name, '~ПРИЕХАЛ К КАМНЮ~')
    print('1 - поехать на арену')
    print('2 - отправиться в таверну')
    print('3 - заглянуть в лавку')
    print('0 - выйти из игры')
    option = input('ВВЕДИТЕ НОМЕР ВАРИАНТА ')
    if option == '1':
        visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength) 
    elif option == '2':
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif option == '3':
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, )
    elif option == '0':
        print('ВЫШЕЛ ИЗ ИГРЫ')
    else:
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    print('ваше здоровье: ', player_hp)
    print('ваша сила: ', player_strength)
    print('ваши деньги: ', player_money)
    print('ваш опыт: ', player_ex)
    print('ваш левл: ', player_level)


def visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    battle = input("вы хотите поучавствовать в сражении за деньги? (y/n) ")
    enemy_hp = 100
    enemy_strength = 100
    if battle == 'y':
        print('вы повстречали врага ')
        print('w - ударить')
        print('q - использовать зелье здоровья')
        print('e - использовать зелье силы')
        print('r - убежать с поля боя')
        while True:
            decision = input('ВЫБИРИТЕ ДЕЙСТВИЕ ')
            if decision == 'w' and player_hp > 0 and enemy_hp > 0:
                your_attack = random.randint(1, player_strength)
                enemy_attack = random.randint(1, enemy_strength)
                print('ваша атака:', your_attack)
                print('атака врага:', enemy_attack)
                player_hp -= enemy_attack
                enemy_hp -= your_attack
                print('ваше здоровье:', player_hp)
                print('здоровье врага:', enemy_hp)
            elif decision == 'q' and player_hp > 0 and enemy_hp > 0:
                print('вы использовали зелье ЗДОРОВЬЯ')
                enemy_attack = random.randint(1, enemy_strength)
                print('атака врага:', enemy_attack)
                player_hp -= enemy_attack
                print('ваше здоровье:', player_hp)
                print('здоровье врага:', enemy_hp)
            elif decision == 'e' and player_hp > 0 and enemy_hp > 0:
                print('вы использовали зелье СИЛЫ')
                enemy_attack = random.randint(1, enemy_strength)
                print('атака врага:', enemy_attack)
                player_hp -= enemy_attack
                print('ваше здоровье:', player_hp)
                print('здоровье врага:', enemy_hp)
            elif decision == 'r' and player_hp > 0 and enemy_hp > 0:
                print('вы убежали ')
                visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
            elif player_hp <= 0:
                print('вы умерли')
            elif enemy_hp <= 0:
                player_ex += 20
                player_money += 20
                print('вы победили врага и получили 20 МОНЕТ и 20 ОПЫТА')
                visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
            else:
                print('у вас опечатка')
                your_attack = random.randint(1, player_strength)
                enemy_attack = random.randint(1, enemy_strength)
                print('ваша атака:', your_attack)
                print('атака врага:', enemy_attack)
                player_hp -= enemy_attack
                enemy_hp -= your_attack
                print('ваше здоровье:', player_hp)
                print('здоровье врага:', enemy_hp)
    elif battle =='n':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:  
        visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, enemy_hp)


def visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    casino = input('вы хотите поиграть в кости на деньги (y/n) ')
    if casino == 'y':
        bot = random.randint(2, 12)
        num = random.randint(2, 12)
        print('ваши деньги:', player_money)
        bet = int(input('ВВЕДИТЕ ВАШУ СТАВКУ: '))
        if player_money >= 1:
            print("ваше число", num)
            print("число бота", bot)
            if num > bot:
                player_money += bet
                print('ВЫ ВЫИГРАЛИ')
                print('ваши деньги:', player_money)  
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)  
            elif num < bot:
                player_money -= bet  
                print('ВЫ ПРОИГРАЛИ')
                print('ваши деньги:', player_money)   
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)    
            else:    
                print('НИЧЬЯ')
                print('ваши деньги:', player_money)
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)
        else:
            print('У ВАС НЕДОСТАТОЧНО ДЕНЕГ ДЛЯ СТАВКИ')
            visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)       
    elif casino == 'n':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength)


def visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength):
    print('q - купить зелье здоровья (10 монет)')
    print('e - купить зелье силы (10 монет)')
    print('r - купить зелье опыта (15 монет)')
    print('w - выйти')
    shopping = input('что бы вы хотели купить? ')
    if shopping == 'q':
        player_hp += 25
        player_money -= 10 
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif shopping == 'e':
        player_strength += 10
        player_money -= 10 
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif shopping == 'r':
        player_ex += 10
        player_money -= 15
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    elif shopping == 'w':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength)
    else:
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength)

start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength)   