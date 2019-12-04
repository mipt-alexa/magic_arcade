import tkinter
import math
import time
from tkinter.filedialog import *



DT = 30
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
dictionary = {}


def catch_message():
    root.after(DT, catch_message)


class Cell:
    def __init__(self):
        self.type = 'Cell'
        self.i = 0
        self.j = 0
        self.color = ''


class Object:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.color = ''


def read_from_file(input_filename):

    global objects
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0]
            if object_type == "Cell":
                cell = Cell()
                parse_sell_parameters(line, cell)
                objects.append(cell)
            # elif object_type == "Planet":
            #     planet = Planet()
            #     parse_planet_parameters(line, planet)
            #     objects.append(planet)
            # else:
            #     print("Unknown space object", object_type)

    return objects


def easy_read(line):
    object_type = line.split()[0]
    if object_type == "Cell":
        cell = Cell()
        parse_sell_parameters(line, cell)
        objects.append(cell)


def parse_sell_parameters(line, cell):
    cellparameters = line.split()
    if cellparameters[0] == "Cell":
        cell.type = cellparameters[0]
        cell.i = int(cellparameters[1])
        cell.j = int(cellparameters[2])
        cell.color = cellparameters[3]


def read_the_line(line):
    print('длина ', len(line))
    list_of_words = line.split()
    print(len(list_of_words))
    for k in range(0, len(list_of_words) - 1):
        if list_of_words[k] == 'obj':
            a = Object()
            a.i = int(list_of_words[k + 1])
            a.j = int(list_of_words[k + 2])
            a.color = list_of_words[k + 3]
            print(a.color)
            objects.append(a)


def draw_grid():
    for i in range(1, 10, 1):
        field.create_line(0, 50*i, 500, 50*i, fill='grey')
    for i in range(1, 10, 1):
        field.create_line(50*i , 0, 50*i, 500, fill='grey')


def main():
    line1 = 'Cell 3 4 orange'
    line2 = 'obj 1 1 red obj 2 3 blue'
    read_the_line(line2)
    for obj in objects:
        print(obj.color)
        field.create_oval(50*obj.i, 50*obj.j, 50*obj.i + 50, 50*obj.j + 50, fill=obj.color)
        print(obj.color)
    draw_grid()
    #field.update()
    #root.after(DT, main)


# a = Cell()
# b = Cell()
# objects.append(a)
# objects.append(b)
main()
root.mainloop()
