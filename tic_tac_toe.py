'''
1 игрок - х
2 игрок - 0
поле из 9 клеток: 3 ряда по 3 клетки 
игроки делают ход по очереди
ход - игрок ставит свой символ в любую свободную клетку
победа: 
    занять любой горизонтальный ряд своими символами 
    занять любую вертикальную колонну своими символами
    занять любую диагональную колонну своими символами
ничья - свободные клетки кончились, а победитель не вывлен победа и ничья прекращают игру

сделать автоматический выбор клетки для компьютерного противника
'''

EMPTY = '.'
PLAYER_1 = 'x'
PLAYER_2 = '0'


def get_field() -> list[str]:
    return [EMPTY] * 9


def drow_field(field: list) -> None:
    '''выводит на экран поле в три ряда по три клетки в каждом'''
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_turn(field: list, player: str) -> None:
    '''спрашивает, в какую клетку поля поставить player
    проверить есть ли такая клетка на поле 
    проверить не занята ли клетка
    если проверка удалась заменить клетку на player'''
    while True:
        try:
            cell_number = int(input('введите номер клетки от 1 до 9 включительно {player}: '))
        except ValueError:
            print('ошибка номер клетки должен быть целым числом')
            continue
        if cell_number > 9 or cell_number < 1:
            print('ошибка клетка должна быть от 1 до 9 включительно')
        elif field[cell_number - 1] != EMPTY:
            print('ошибка клетка занята')
        else:
            field[cell_number - 1] = player
            break


def get_winner(field: list[str], player: str) -> str:
    '''
    возвращает player, если он занял хотя бы один ряд колонну или диагональ
    '''
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player


    for i in range(3):
        if field[i] == field[i + 3] == field[i + 6] == player:    
            return player
        
    if field[0] == field[4] == field[8] == player:    
        return player    

    if field[2] == field[4] == field[6] == player:    
        return player  
    
    return ''


def main():
    '''главная функция'''
    field = get_field()
    turn = 1
    while turn <= 9:
        drow_field(field)
        if turn % 2:
            player = PLAYER_1 # 'x'
        else:
            player = PLAYER_2 # '0'

        make_turn(field, player)
        turn += 1
        winner = get_winner(field, player)
        if winner:
            drow_field(field)
            print(f'игра окончена победил {player}')
            break 
    else: 
        drow_field(field)
        print('игра окончена. ничья')

main()