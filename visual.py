import tkinter
from tkinter.filedialog import *
from Battlefield_class import*
from Cells_classes import *
from Spell_classes import *




def create_field_image():
    """Создаёт картинку клеточного поля""" #TODO
    pass

def create_obj_image(field, object):
    """Создаёт картинку игроков, препятствий, целей""" #TODO
    x = object.x
    y = object.y
    field.coords(object.image, object.x, object.y, object.x + 10, object.y + 10)
    pass