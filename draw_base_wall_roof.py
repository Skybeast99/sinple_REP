import turtle

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
    roof_w=100,
    roof_h=100, 
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

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_c - цвет крыши
    '''
    print('начинаем стоить дом')
    draw_base(x, y, base_w, base_h, base_c)
    draw_wall(x, y, wall_w, wall_h, wall_c, base_h)
    draw_roof(x, y, roof_w, roof_h, roof_c, base_h, wall_h, wall_w)


def draw_base(x, y, width, height, color):
    '''рисует фундамент'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_wall(x, y, width, height, color, base_h):
    '''рисует стены'''
    turtle.penup()
    turtle.goto(x, y + base_h)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_roof(x, y, width, height, color, wall_h, base_h, wall_w):
    '''рисует крышу'''
    turtle.penup()
    roof_y = y + base_h + wall_h
    turtle.goto(x, roof_y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    x_top = x + wall_w // 2
    y_top = y + height + wall_h
    turtle.goto(x_top, y_top)
    turtle.goto(x_top + wall_w // 2, roof_y)
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


draw_house()
draw_house(x=50, y=130, base_c='green', wall_c='purple', roof_c='brown')
draw_house(x=70, y=-140, base_c='orange', wall_c='pink', roof_c='yellow')
draw_house(x=-198, y=5, base_c='grey', wall_c='black', roof_c='white')
draw_house(x=-88, y=-100)
draw_house(x=199, y=-19)
draw_house(x=-250, y=-176)

turtle.done()