import os
import random


def pause ():
    print(input)

player_name = 'пипяо'
game = False
player_hp = 250
player_strength = 100
player_money = 10
player_ex = 1
player_level = 1
player_potion = 0
player_potion_1 = 0
healpoint = 250

def start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1):
    player_name = input('~ВВЕДИТЕ ВАШЕ ИМЯ~: ')
    player_hp = 250
    player_strength = 100
    player_money = 15
    player_ex = 0
    player_level = 1
    player_potion = 0
    player_potion_1 = 0
    visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)


def visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1):
    os.system('cls')
    show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1, healpoint) 
    print(player_name, '~ПРИЕХАЛ К КАМНЮ~')
    print('1 - поехать на арену')
    print('2 - отправиться в таверну')
    print('3 - заглянуть в лавку')
    print('0 - выйти из игры')
    option = input('ВВЕДИТЕ НОМЕР ВАРИАНТА ')
    if option == '1':
        visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    elif option == '2':
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    elif option == '3':
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    elif option == '0':
        print('ВЫШЕЛ ИЗ ИГРЫ')
    else:
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)


def show_hero(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1, healpoint):
    if player_ex < player_level * 100:
        print('ваше здоровье: ', player_hp)
        print('ваша сила: ', player_strength)
        print('ваши деньги: ', player_money)
        print('ваш опыт: ', player_ex)
        print('ваш левл: ', player_level)
        print('ваши зелья здоровья: ', player_potion)
        print('ваши зелья силы: ', player_potion_1)
    else:
        player_level += 1 
        player_strength += 10
        healpoint += 25
        player_hp += 25
        print('ВАШ ЛЕВЛ ПОВЫШЕН')
        print('ВАШ УРОН И УРОВЕНЬ МАКСИМАЛЬНОГО ЗДОРОВЬЯ ПОВЫШЕН')
        print('ваше здоровье: ', player_hp)
        print('ваша сила: ', player_strength)
        print('ваши деньги: ', player_money)
        print('ваш опыт: ', player_ex)
        print('ваш левл: ', player_level)
        print('ваши зелья здоровья: ', player_potion)
        print('ваши зелья силы: ', player_potion_1)
    return player_level


def visit_battle(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1):
    battle = input("вы хотите поучавствовать в сражении за деньги? (y/n) ")
    enemy_hp = 100
    enemy_strength = 100
    enemy_xp = 0
    enemy_level = 1
    if battle == 'y':
        print('вы повстречали врага ')
        print('w - ударить')
        print('q - использовать зелье здоровья')
        print('e - использовать зелье силы')
        print('r - убежать с поля боя')
        while True:
            print('ваши зелья здоровья: ', player_potion)
            print('ваши зелья силы: ', player_potion_1)
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
                if player_potion <= 0:
                    print('У ВАС НЕТ ЗЕЛЕЙ ЗДОРОВЬЯ')
                else:
                    print('вы использовали зелье ЗДОРОВЬЯ')
                    if player_hp <= 100:
                        player_hp += 150
                        player_potion -= 1
                        enemy_attack = random.randint(1, enemy_strength)
                        print('атака врага:', enemy_attack)
                        player_hp -= enemy_attack
                        print('ваше здоровье:', player_hp)
                        print('здоровье врага:', enemy_hp)
                    else:
                        damage = healpoint - player_hp
                        player_hp += damage
                        player_potion -= 1
                        enemy_attack = random.randint(1, enemy_strength)
                        print('атака врага:', enemy_attack)
                        player_hp -= enemy_attack
                        print('ваше здоровье:', player_hp)
                        print('здоровье врага:', enemy_hp)
            elif decision == 'e' and player_hp > 0 and enemy_hp > 0:
                if player_potion_1 <= 0:
                    print('У ВАС НЕТ ЗЕЛЕЙ СИЛЫ')
                else:
                    print('вы использовали зелье СИЛЫ')
                    player_strength += 15
                    player_potion_1 -= 1
                    enemy_attack = random.randint(1, enemy_strength)
                    print('атака врага:', enemy_attack)
                    player_hp -= enemy_attack
                    print('ваше здоровье:', player_hp)
                    print('здоровье врага:', enemy_hp)
            elif decision == 'r' and player_hp > 0 and enemy_hp > 0:
                print('вы убежали ')
                visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
            elif player_hp <= 0:    
                print('ВЫ УМЕРЛИ')
            elif enemy_hp <= 0:
                player_ex += 20
                player_money += 15
                print('вы победили врага и получили 15 МОНЕТ и 20 ОПЫТА')
                visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
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
    elif battle == 'n':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    else:  
        print('опечатка')
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    os.system('cls')


def visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1):
    casino = input('вы хотите поиграть в кости на деньги (y/n) ')
    if casino == 'y':
        bot = random.randint(2, 12)
        num = random.randint(2, 12)
        print('ваши деньги:', player_money)
        bet = input('ВВЕДИТЕ ВАШУ СТАВКУ: ')

        try:
            bet = int(bet)
        except ValueError:
            print('У ВАС ОШИБКА!!!')
            visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)

        if player_money >= 1:
            print("ваше число", num)
            print("число бота", bot)
            if num > bot:
                player_money += bet
                print('ВЫ ВЫИГРАЛИ')
                print('ваши деньги:', player_money)  
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)  
            elif num < bot:
                player_money -= bet  
                print('ВЫ ПРОИГРАЛИ')
                print('ваши деньги:', player_money)   
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)    
            else:    
                print('НИЧЬЯ')
                print('ваши деньги:', player_money)
                visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
        else:
            print('У ВАС НЕДОСТАТОЧНО ДЕНЕГ ДЛЯ СТАВКИ')
            visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)       
    elif casino == 'n':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    else:
        visit_tavern(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    os.system('cls')


def visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1):
    print('q - купить зелье здоровья (15 монет)')
    print('e - купить зелье силы (10 монет)')
    print('r - купить зелье опыта (15 монет)')
    print('w - выйти')
    potion_prize_h = 15
    potion_prize_s = 10
    shopping = input('что бы вы хотели купить? ')
    if shopping == 'q':
        if player_money < potion_prize_h:
            print(f'У {player_name} НЕДОСТАТОЧНО ДЕНЕГ')
        else:
            player_money -= potion_prize_s
            player_potion += 1
        pause()
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)    
    elif shopping == 'e':
        if player_money < potion_prize_s:
            print(f'У {player_name} НЕДОСТАТОЧНО ДЕНЕГ')
        else:
            player_money -= potion_prize_s
            player_potion_1 += 1
        pause()
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    elif shopping == 'r':
        if player_money < potion_prize_h:
            print(f'У {player_name} НЕДОСТАТОЧНО ДЕНЕГ')
        else:
            player_ex += 10
            player_money -= 15
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    elif shopping == 'w':
        visit_rock(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    else:
        visit_lavka(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1)
    os.system('cls') 

start_game(player_name, player_hp, player_money, player_ex, player_level, player_strength, player_potion, player_potion_1) 