from tkinter import *
from PIL import ImageTk,Image


"""1 = камущки """
""" 2  = маг в красном """

images = []
N = 2
"""число картинок"""


def load_image(canv):
    """загружает все изображения, должна быть вызвана в начале 1 раз"""
    global images1
    path = str(1) + ".jpg"
    images1 = ImageTk.PhotoImage(Image.open(path), canv)
    path = str(2) + ".jpg"
    images2 = ImageTk.PhotoImage(Image.open(path), canv)
    print('tried to load')


def get_image(k):
    """возвращает объект картинку"""
    global images1
    return images1


