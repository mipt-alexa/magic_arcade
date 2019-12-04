import tkinter
import math
import time
from tkinter.filedialog import *


DT = 1
"""тик времени"""
header_font = "Arial-16"
"""Шрифт в заголовке"""
window_width = 500
"""Ширина окна"""
window_height = 500
"""Высота окна"""


root = tkinter.Tk()
field = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
field.pack(fill=tkinter.BOTH, expand=1)

objects = []
messages_to_send =[]
message_to_server = ''


class Object:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.color = ''

    def draw(self):
        field.create_oval(50*self.i, 50*self.j, 50*self.i - 50, 50*self.j - 50, fill=self.color)



def read_the_line(line):
    """Строку от сервера делит на слова, созвдает объеты класса Obj, записывает признаки"""
    list_of_words = line.split()
    if list_of_words[0] == 'obj':
            a = Object()
            a.i = int(list_of_words[1])
            a.j = int(list_of_words[2])
            a.color = list_of_words[3]
            objects.append(a)


def draw_grid():
    for i in range(1, 10, 1):
        field.create_line(0, 50*i, 500, 50*i, fill='grey')
    for i in range(1, 10, 1):
        field.create_line(50*i , 0, 50*i, 500, fill='grey')


def click_processing(event):
    """Обрабывает данные от клика. Дописывает в строку, строку добавляет в массив """
    event_i = event.x // 50 + 1
    event_j = event.y // 50 + 1
    message_to_server = 'click ' + str(event_i) + ' ' + str(event_j) + ' '
    messages_to_send.append(message_to_server)


def binding():
    field.bind('<Button-1>', click_processing)


def get_from_server():
    """Получает массив строк(?) от сервер"""
    pass


def send_to_server():
    """Отправляет массив строк на сервер"""
    pass


def main():

    binding()
    for obj in objects:
        obj.draw()

    field.update()
    root.after(DT, main)




draw_grid()
main()
root.mainloop()
