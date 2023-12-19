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
    print('q - купить товары')
    print('w - продать товары')
    print('e - выйти из лавки')
    option = input('введите номер опции: ')
    if option == 'q':
        for num, item in enumerate(shop_items):
            print(f'{num} - {item}')
        print('0 - выйти из покупки или продажи')
        option = input('введите номер опции: ')

player = get_hero(name='вася')  
shop_items = ['зелье лечения', 'зелье силы', 'опыт']
visit_shop(player, shop_items)