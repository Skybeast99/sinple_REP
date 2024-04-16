import tkinter


questions = [
    {
        'текст вопроса': 'какой оператор умножает числа в питоне?',
        'варианты ответов': ['*', '**', 'x', '//'],
        'индекс правильного ответа': 3
    },
    {
        'ВОПРОС': 'какой из этих типов изменяется',
        'ответы': ["list", "str", "tuple", "int"],
        'индекс правильного ответа': 0
    }


]


class App:
    """
    приложение
    TODO: окно во весь экран
    """
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Consolas', 30))
        self.width = self.window.winfo_screenwidth()
        self.hight = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.hight}')
        self.lable_question_text = None
        self.lable_answer_1_text = None
        self.lable_answer_2_text = None
        self.lable_answer_3_text = None
        self.lable_answer_4_text = None
        self.button_answer_1 = None
        self.button_answer_2 = None
        self.button_answer_3 = None
        self.button_answer_4 = None
        self.make_widgets()
        self.position_widgers()
        self.make_pack()
        self.start()
        self.window.mainloop()

    def make_widgets(self) -> None:
        '''создает экземпляры виджетов'''
        self.lable_question_text = tkinter.Label(self.window)
        self.lable_answer_1_text = tkinter.Label(self.window)
        self.lable_answer_2_text = tkinter.Label(self.window)
        self.lable_answer_3_text = tkinter.Label(self.window)
        self.lable_answer_4_text = tkinter.Label(self.window)
        self.button_answer_1 = tkinter.Button(self.window)
        self.button_answer_2 = tkinter.Button(self.window)
        self.button_answer_3 = tkinter.Button(self.window)
        self.button_answer_4 = tkinter.Button(self.window)

    def position_widgers(self) -> None:
        '''позиционирует виджеты'''
        self.lable_question_text = tkinter.Label(self.window)
        self.lable_answer_1_text = tkinter.Label(self.window)
        self.lable_answer_2_text = tkinter.Label(self.window)
        self.lable_answer_3_text = tkinter.Label(self.window)
        self.lable_answer_4_text = tkinter.Label(self.window)
        self.button_answer_1 = tkinter.Button(self.window, text='1',command=lambda: self.on_click(1))
        self.button_answer_2 = tkinter.Button(self.window, text='2', command=lambda: self.on_click(2))
        self.button_answer_3 = tkinter.Button(self.window, text='3', command=lambda: self.on_click(3))
        self.button_answer_4 = tkinter.Button(self.window, text='4', command=lambda: self.on_click(4))
    
    def make_pack(self) -> None:
        self.lable_question_text.pack()
        self.lable_answer_1_text.pack()
        self.lable_answer_2_text.pack()
        self.lable_answer_3_text.pack()
        self.lable_answer_4_text.pack()
        self.button_answer_1.pack()
        self.button_answer_2.pack()
        self.button_answer_3.pack()
        self.button_answer_4.pack()

    def start(self) -> None:
        self.question_number = 0
        self.lable_question_text['text'] = questions[self.question_number]['текст вопроса']
        self.lable_answer_1_text['text'] = '1. ' + questions[self.question_number]['варианты ответов'][0]
        self.lable_answer_2_text['text'] = '2. ' + questions[self.question_number]['варианты ответов'][1]
        self.lable_answer_3_text['text'] = '3. ' + questions[self.question_number]['варианты ответов'][2]
        self.lable_answer_4_text['text'] = '4. ' + questions[self.question_number]['варианты ответов'][3]

    def on_click(self, button_number: int) -> None:
        print('кнопка нажата', button_number)
        # TODO: сравнить номер кнопки с индексом правильного ответа

App()