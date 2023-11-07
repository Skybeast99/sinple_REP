import turtle

def draw_base(width, hight, color):

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

draw_base(10, 200, 'red')
draw_base(20, 100, 'white')
draw_base(12, 300, 'green')
draw_base(15, 150, 'black') 
turtle.done()