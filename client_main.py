import tkinter
import math
import time
import random as rnd
from tkinter.filedialog import *
import connection as con

DT = 10
"""тик времени"""
header_font = "Arial-16"
"""Шрифт в заголовке"""
window_width = 500
"""Ширина окна"""
window_height = 500
"""Высота окна"""


class Object:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.color = ''


def read_message():
    list_of_messages = con.read_message('server')
    return list_of_messages


def send_message(message):
    con.write_message('client', message)


def click_processing(event):
    """Обрабывает данные от клика. Дописывает в строку, строку добавляет в массив """
    event_i = event.x // 50 + 1
    event_j = event.y // 50 + 1
    message_to_server = 'click ' + str(event_i) + ' ' + str(event_j) + ' '
    send_message(message_to_server)


class ClientGameApp:
    def __init__(self):
        self.root = tkinter.Tk()
        self.field = tkinter.Canvas(self.root, width=window_width, height=window_height, bg="black")
        self.field.pack(fill=tkinter.BOTH, expand=1)
        self.objects = []

    def draw_object(self, obj):
        self.field.create_oval(50 * self.i, 50 * self.j, 50 * self.i - 50, 50 * self.j - 50, fill=self.color)

    def process_message(self, message):
        """Строку от сервера делит на слова, созвдает объеты класса Obj, записывает признаки"""
        list_of_words = message.split()
        if list_of_words[0] == 'obj':
            a = Object()
            a.i = int(list_of_words[1])
            a.j = int(list_of_words[2])
            a.color = list_of_words[3]
            self.objects.append(a)

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
                self.process_message()
                for obj in self.objects:
                    self.draw_object(obj)
        self.root.after(DT, self.update)


app = ClientGameApp()
app.draw_grid()
app.update()
app.root.mainloop()
