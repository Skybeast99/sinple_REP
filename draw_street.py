import turtle
import random

num_house = int(input('введите колличество домов '))
n = 0
x_house = -600

turtle.speed(0)


def draw_house(
    x=0,
    y=0,
    base_w=100,
    base_h=5,
    base_c='green',
    wall_w=100,
    wall_h=60,
    wall_c='blue',
    door_w=20, 
    door_h=30, 
    door_c='yellow', 
    roof_w=100,
    roof_h=50, 
    roof_c='red'
    ):
    '''
    вызывает функцию рисования фундамента
    вызывает функцию рисования стен
    вызывает функцию рисования крыши
    
    x - левый нижний угол фундамента
    y - левый нижний угол фундамента

    base_w - ширина фундамента
    base_h- высота фундамента
    base_c - цвет фундамента

    wall_w - ширина стены
    wall_h - высота стены
    wall_c - цвет стены

    door_w - ширина стены
    door_h - высота стены
    door_c - цвет стены

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_c - цвет крыши
    '''
    print('начинаем стоить дом')
    draw_base(x, y, base_w, base_h, base_c)
    draw_wall(x, y, wall_w, wall_h, wall_c, base_h)
    draw_door(x, y, door_w, door_h, door_c, base_h, wall_w)
    draw_roof(x, y, roof_w, roof_h, roof_c, base_h, wall_h, wall_w)


def draw_base(x, y, width, height, color):
    '''рисует фундамент'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_wall(x, y, width, height, color, base_w):
    '''рисует стены'''
    turtle.penup()
    turtle.goto(x, y + base_w)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_door(x, y, width, height, color, base_w, wall_w):
    turtle.penup()
    turtle.goto(x + wall_w // 2 - width // 2, y + base_w)
    turtle.pendown()    
    draw_rectangle(width, height, color)

def draw_roof(x, y, width, height, color, wall_h, base_h, wall_w):
    '''рисует крышу'''
    turtle.penup()
    roof_y = y + base_h + wall_h
    turtle.goto(x + wall_w // 2 - width // 2, roof_y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    x_top = x + wall_w // 2
    y_top = y + height + wall_h + base_h
    turtle.goto(x_top, y_top)
    turtle.goto(x_top + width // 2, roof_y)
    turtle.goto(x, roof_y)
    turtle.end_fill()


def  draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)   
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()

while n < num_house:
    width = random.randint(50, 100)
    height = random.randint(50, 100)
    color = ['green', 'blue', 'black', 'orange', 'red', 'yellow']

    draw_house(
    x=x_house,
    y=0,
    base_w=width,
    base_h=random.randint(height // 100 * 10, height // 10 * 20),
    base_c='green',
    wall_w=random.randint(50, width),
    wall_h=random.randint(50, 100),
    wall_c='blue',
    door_w=(width // 100 * 20, width // 100 * 30), 
    door_h=random.randint(height //100 * 20, height // 100 * 40), 
    door_c='yellow', 
    roof_w=random.randint(width, width // 100 * 120),
    roof_h=random.randint(height // 100 * 25, height // 100 * 75), 
    roof_c='red')
    n += 1
    x_house += 101

turtle.done()