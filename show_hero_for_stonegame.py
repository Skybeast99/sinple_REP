from random import choice


def get_hero (name=None, hp=100, level=1, xp=0, money=25, inventory=None) -> list:
    '''возвращает список харрактеристик героя '''
    if not name:
        names = ('ok', 'not ok', 'fine', 'олег')
        name = choice(names)
    if not inventory:
        inventory = []
    return [name, hp, level, xp, money, inventory]

def show_hero(hero: list) -> None:
    ''' выводит на экран харрактеристики персонажа построчно '''
    print('имя:', hero[0])
    print('здоровье:', hero[1])
    print('уровень:', hero[2])
    print('опыт:', hero[3])
    print('деньги:', hero[4])
    print('инвентарь:', hero[5])


def show_enumirated_items(items: list) -> None:
    ''' выводит на экран проумерованные предметы '''
    for num, item in enumerate(items, 1):
        print(f'{num} - {item}')

def get_option(items: list) -> str
    '''  '''
    print('0 - отмена')
    option = input('введите номер опции: ')
    if option == '0':
        print('отмена поупки')
        return ''
    elif int(option) < 0 or int(option) > len(shop_items):
        print('ошибка неверная опция')
        return ''
    else:
        return option

def visit_shop(hero: list, shop_items):
    '''выводит информацию о герое
    выводит на экран текст магазина
    выводит на экран текст магазина
    выводит на экран опции
    предоставляет игроку выбор опции
    действует по выбранной опции
    '''
    shop_items = ['зелье лечения', 'зелье силы', 'опыт']
    show_hero(hero)
    print(f'{hero[0]} приехал в лавку торговца')
    price_tmp = 10
    print('1 - купить товары')
    print('2 - продать товары')
    print('0 - выйти из лавки')
    option = input('введите номер опции: ')
    if option == '1':
        show_enumirated_items(shop_items)
        option = get_option(shop_items)
    else:
        hero[4] -= price_tmp
        item_index = int(option) - 1
        item_name = shop_items[item_index]
        hero[5].append(item_name)
        shop_items.pop(item_index)


        print(hero[0], 'купил', shop_items[int(option) - 1])


player = get_hero(name='вася')
shop_items = ['зелье лечения', 'зелье силы', 'опыт']
visit_shop(player, shop_items)
print('конец')
