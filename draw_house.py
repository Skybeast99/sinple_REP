import turtle

def draw_base(width, hight, color, x, y):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)

    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(hight)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(hight)
    turtle.left(90)

    turtle.end_fill()

draw_base(10, 200, 'red', 100, 150)
draw_base(20, 100, 'white', 110, 30)
draw_base(12, 300, 'green', 120, -50)
draw_base(15, 150, 'black', 70, 80) 
turtle.done()