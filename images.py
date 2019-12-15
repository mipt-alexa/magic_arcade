from tkinter import *
from PIL import ImageTk,Image
# -*- coding: utf-8 -*-

""" 1 = камушки """
""" 2  = стена """
""" 3 = deep elf demonologist"""
""" 4 = deep elf mage"""
""" 5 = walk"""
""" 6 = fireball"""
""" 7 = ice_spike"""
""" 8 = wall"""
""" 9 = 0"""
""" 10 = 1"""
""" 11 = 2"""
N = 11
"""число картинок"""
images = {}


def load_all_images(canv):
    """загружает все изображения, должна быть вызвана сразу после иницализации app"""
    global images
    path = "images_library/" + 'mage1' + ".png"
    images['mage1'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'mage2' + ".png"
    images['mage2'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'wall' + ".png"
    images['wall'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'floor' + ".png"
    images['floor'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'walk' + ".png"
    images['walk'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'ice spike' + ".png"
    images['ice spike'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + '0' + ".png"
    images['0'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + '1' + ".png"
    images['1'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + '2' + ".png"
    images['2'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + '3' + ".png"
    images['3'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'fireball' + ".png"
    images['fireball'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'wall spell' + ".png"
    images['wall spell'] = (ImageTk.PhotoImage(Image.open(path), canv))
    path = "images_library/" + 'cursor' + ".png"
    images['cursor'] = (ImageTk.PhotoImage(Image.open(path), canv))

def get_image(k):
    """возвращает объект картинку"""
    global images
    return images[k]


