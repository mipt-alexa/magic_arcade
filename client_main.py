import tkinter
import math
import time
import random as rnd
from tkinter.filedialog import *
import connection as con
from Mage_class import BASIC_ENERGY, BASIC_HEALTH

DT = 10
"""тик времени"""
header_font = "Arial-16"
"""Шрифт в заголовке"""
window_width = 500
"""Ширина окна"""
window_height = 500
"""Высота окна"""
interface_height = 100


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
        self.interface = tkinter.Canvas(self.root, width=window_width, height=interface_height, bg="black")
        self.interface.pack(fill=tkinter.BOTH, expand=1, side=BOTTOM)
        self.field.pack(fill=tkinter.BOTH, expand=1)
        self.objects = {}
        self.health_bar1_id = None
        self.health_bar2_id = None
        self.energy_bar1_id = None
        self.energy_bar2_id = None

    def draw_object(self, obj):
        canvas_id = self.field.create_oval(50 * obj.x, 50 * obj.y, 50 * obj.x + 50, 50 * obj.y + 50, fill=obj.color)
        return canvas_id

    def draw_bars(self):
        self.health_bar1_id = self.interface.create_line(0, 15, 200, 15, width=15, fill='red')
        self.health_bar2_id = self.interface.create_line(window_width - 200, 15, window_width, 15, width=15, fill='red')
        self.energy_bar1_id = self.interface.create_line(0, 35, 200, 35, width=15, fill='grey')
        self.energy_bar2_id = self.interface.create_line(window_width - 200, 35,  window_width, 35, width=15, fill='grey')

    def set_energy(self, player, energy):
        if player == 'player1':
            self.interface.coords(self.energy_bar1_id, 0, 35, energy / BASIC_ENERGY * 200, 35)
        elif player == 'player2':
            self.interface.coords(self.energy_bar2_id, window_width - energy / BASIC_ENERGY * 200, 35, window_width, 35)

    def set_health(self, player, health):
        if player == 'player1':
            self.interface.coords(self.energy_bar1_id, 0, 35, health / BASIC_ENERGY * 200, 35)
        elif player == 'player2':
            self.interface.coords(self.energy_bar2_id, window_width - health / BASIC_ENERGY * 200, 35, window_width, 35)

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
        if list_of_words[0] == 'set_energy':
            self.set_energy(list_of_words[1], int(list_of_words[2]))

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
                self.process_message(message)
        self.root.after(DT, self.update)


app = ClientGameApp()
app.bind_all()
app.draw_grid()
app.draw_bars()
app.update()
app.root.mainloop()
