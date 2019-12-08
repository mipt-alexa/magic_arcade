import tkinter
import math
import time
import random as rnd
from tkinter.filedialog import *
import connection as con
from PIL import Image, ImageTk
import images as img


DT = 10
"""тик времени"""
header_font = "Arial-16"
"""Шрифт в заголовке"""
cell_size = 34
"""Размер клетки"""
width = 15
"""ширина в клетках"""
window_width = width*cell_size
"""Ширина окна"""
height = 15
window_height = height*cell_size
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
        self.root.wm_title("Magic!")
        self.field = tkinter.Canvas(self.root, width=window_width, height=window_height, bg="black")
        self.field.pack(fill=tkinter.BOTH, expand=1)
        self.objects = {}

    # def draw_object(self, obj):
    #     canvas_id = self.field.create_image(obj.x, obj.y, anchor=NW, image=lib.get_image(#FIXME здесь
    #      должен быть номер картинки))
    #     return canvas_id


    def process_message(self, message):
        """Строку от сервера делит на слова, созвдает объеты класса Obj, записывает признаки"""
        list_of_words = message.split()
        if list_of_words[0] == 'obj':
            a = Object()
            a.client_id = int(list_of_words[1])
            a.x = int(list_of_words[2])*cell_size - 1
            a.y = int(list_of_words[3])*cell_size - 1
            a.color = list_of_words[4]
            if self.objects.get(a.client_id) is not None:
                self.field.delete(self.objects[a.client_id].canvas_id)
            a.canvas_id = self.draw_object(a)
            self.objects[a.client_id] = a

    def draw_grid(self):
        """Рисует сетку и камушки"""
        for i in range(0, window_width // cell_size + 1, 1):
            self.field.create_line(0, cell_size * i, window_height, cell_size * i, fill='grey')
            for j in range(0, window_height // cell_size + 1, 1):
                self.field.create_image(i * cell_size + 1, j * cell_size + 1, anchor=NW, image=img.get_image(1))
                self.field.create_line(cell_size * j, 0, cell_size * j, window_width, fill='grey')

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
img.load_all_images(app)

app.bind_all()
app.draw_grid()

img2 = img.get_image(2) #test
app.field.create_image(15, 15, anchor=NW, image=img2) #test

app.update()
app.root.mainloop()
