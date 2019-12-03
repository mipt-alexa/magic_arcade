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


class Sell:
    def __init__(self, i, j):
        self.type = 'Sell'
        self.i = i
        self.j = j


def read_from_file(input_filename):

    global objects
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0]
            if object_type == "Sell":
                sell = Sell()
                parse_sell_parameters(line, sell)
                objects.append(sell)
            # elif object_type == "Planet":
            #     planet = Planet()
            #     parse_planet_parameters(line, planet)
            #     objects.append(planet)
            # else:
            #     print("Unknown space object", object_type)

    return objects


def parse_sell_parameters(line, sell):

    sellparameters = line.split()
    if sellparameters[0] == "Sell":
        sell.type = sellparameters[0]
        sell.i = sellparameters[1]
        sell.j = sellparameters[2]


def main():
    for obj in objects:
        field.create_oval(50*obj.i, 50*obj.j , 50*obj.i + 50, 50*obj.j + 50, fill='white')
    #field.update()
    #root.after(DT, main)


a = Sell(1, 2)
b = Sell(3,7)
objects.append(a)
objects.append(b)
main()
root.mainloop()
