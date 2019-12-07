import tkinter
import math
import time
import random as rnd
from tkinter.filedialog import *
import connection as con

DT = 1
"""тик времени"""
header_font = "Arial-16"
"""Шрифт в заголовке"""
window_width = 500
"""Ширина окна"""
window_height = 500
"""Высота окна"""


class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.client_id = None
        self.color = ''
        self.canvas_id = None


def read_message():
    list_of_messages = con.read_message('client')
    return list_of_messages


def send_message(message):
    con.write_message('client', message)


def click_processing(event):
    """Обрабывает данные от клика. Дописывает в строку, строку добавляет в массив """
    event_x = event.x // 50
    event_y = event.y // 50
    message_to_server = 'click ' + str(event_x) + ' ' + str(event_y) + ' '
    send_message(message_to_server)


class ClientGameApp:
    def __init__(self):
        self.root = tkinter.Tk()
        self.field = tkinter.Canvas(self.root, width=window_width, height=window_height, bg="black")
        self.field.pack(fill=tkinter.BOTH, expand=1)
        self.objects = {}

    def draw_object(self, obj):
        canvas_id = self.field.create_oval(50 * obj.x, 50 * obj.y, 50 * obj.x + 50, 50 * obj.y + 50, fill=obj.color)
        return canvas_id

    def process_message(self, message):
        """Строку от сервера делит на слова, созвдает объеты класса Obj, записывает признаки"""
        list_of_words = message.split()
        if list_of_words[0] == 'obj':
            a = Object()
            a.client_id = int(list_of_words[1])
            a.x = int(list_of_words[2])
            a.y = int(list_of_words[3])
            a.color = list_of_words[4]
            if self.objects.get(a.client_id) is not None:
                self.field.delete(self.objects[a.client_id].canvas_id)
            a.canvas_id = self.draw_object(a)
            self.objects[a.client_id] = a

    def draw_grid(self):
        for i in range(1, 10, 1):
            self.field.create_line(0, 50 * i, 500, 50 * i, fill='grey')
        for i in range(1, 10, 1):
            self.field.create_line(50 * i, 0, 50 * i, 500, fill='grey')

    def bind_all(self):
        self.field.bind('<Button-1>', click_processing)

    def update(self):
        list_of_messages = read_message()
        if len(list_of_messages) > 0:
            for message in list_of_messages:
                if message == '':
                    continue
                print(message)
                self.process_message(message)
        self.root.after(DT, self.update)



app = ClientGameApp()
app.bind_all()
app.draw_grid()
app.update()
app.root.mainloop()
