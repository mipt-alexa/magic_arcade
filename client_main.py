import tkinter
import math
import time
from tkinter.filedialog import *



DT = 10
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


class Cell:
    def __init__(self):
        self.type = 'Cell'
        self.i = 0
        self.j = 0


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


def draw_grid():
    for i in range(1, 10, 1):
        field.create_line(0, 50*i, 500, 50*i, fill='grey')
    for i in range(1, 10, 1):
        field.create_line(50*i , 0, 50*i, 500, fill='grey')

def main():
    line1 = 'Cell 3 4'
    easy_read(line1)
    for obj in objects:
        field.create_oval(50*obj.i, 50*obj.j, 50*obj.i + 50, 50*obj.j + 50, fill='white')
    draw_grid()
    #field.update()
    #root.after(DT, main)


# a = Cell()
# b = Cell()
# objects.append(a)
# objects.append(b)
main()
root.mainloop()
