# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk,Image

""" 1 = камушки """
""" 2  = стена """
""" 3 = deep elf demonologist"""
"""" 4 = deep elf mage"""


N = 4
"""число картинок"""
images = [None]


def load_all_images(canv):
    """загружает все изображения, должна быть вызвана сразу после иницализации app"""
    global images
    for i in range(1, N+1):
        path = "images_library/" + str(i) + ".png"
        images.append(ImageTk.PhotoImage(Image.open(path), canv))
        print('tried to load')     #testing


def get_image(k):
    """возвращает объект картинку"""
    global images
    return images[k]


