import tkinter


def on_click_1(*event) -> None:
    print('кнопка нажата')
    lable_1.config(bg='red')
    lable_2.config(bg='blue')


def on_click_2(*event) -> None:
    print('кнопка нажата')
    lable_1.config(bg='blue')
    lable_2.config(bg='red')


def window_change_color(event) -> None:
    window['bg'] = 'black'


window = tkinter.Tk()
window.geometry('500x500')
window.title('мое графическое окно')
window['padx'] = 30
window['pady'] = 30
window.bind('<Key>', window_change_color)

lable_1 = tkinter.Label(window, text='текст метки 1')
lable_2 = tkinter.Label(window, text='текст метки 2') 

button_1 = tkinter.Button(window, text='поменять цвет', command=on_click_1)
button_2 = tkinter.Button(window, text='поменять цвет', command=on_click_2)

lable_1.config(bg='blue')
lable_2.config(bg='red')

lable_1['font'] = ('Impact', 15)
lable_2['font'] = ('Impact', 15)
lable_1.bind('<Button-1>', on_click_1)
lable_2.bind('<Button-1>', on_click_2)

lable_1.pack(side='left', expand=True, fill='both')
lable_2.pack(side='right', expand=True, fill='both')
button_1.pack()
button_2.pack()

window.mainloop()
