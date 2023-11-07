import turtle

def draw_house(
    x=0,
    y=0,
    base_w=100,
    base_h=100,
    base_c='blue',
    wall_w=100,
    wall_h=60,
    wall_c='blue',
    roof_w=100,
    roof_h=10, 
    roof_c='blue'):
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

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_c - цвет крыши
    '''
    print('начинаем стоить дом')
    draw_base(12, 70, 'blue', 1, 1)
    draw_wall()
    draw_roof()

def draw_base(width, height, color, x, y):
    '''рисует фундамент'''
    print('рисует фундамент')

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)

def  draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill(color)
    turtle.fd(width)
    turtle.lt(90)   
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill(color)


def draw_wall(wall_w, wall_h, wall_c):
    '''рисует стены'''
    print('рисует стены')

def draw_roof(roof_w, roof_h, roof_c):
    '''рисует крышу'''
    print('рисует крышу')

turtle.done()
draw_house()