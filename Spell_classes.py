#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Данные классы являются неким конструктром заклинаний.
Сами саклинания будут создаваться как обЪекты этих классов с заданными параметрами.
Эти обЪекты будут храниться в отдельном словаре или даже файле с названием spell_book.
"""


class Spell:
    def __init__(self, name, energy, menu_image_id, sound):
        self.type = 'spell'
        self.energy = energy
        self.name = name
        self.menu_image_id = menu_image_id
        self.sound = sound



class DirectSpell(Spell):
    """
    Класс направленного заклинания, которое применяется на некоторый объект (маг ил препятствие) или клетку
    """
    def __init__(self, name, energy, menu_image_id, sound, spell_range):
        super().__init__(name, energy, menu_image_id, sound)
        self.spell_range = spell_range


class AttackDirectSpell(DirectSpell):
    """
    Направленное заклинание, наносящее урон
    """
    def __init__(self, name, energy, menu_image_id, sound, spell_range, health_damage, energy_damage, destination):
        super().__init__(name, energy, menu_image_id, sound, spell_range)
        self.spell_type = 'attack_directed'
        self.destination = destination # тип объекта на который может быть направленно заклинание(Mage, Obstacle, Both)
        self.health_damage = health_damage
        self.energy_damage = energy_damage


class DefendDirectSpell(DirectSpell):
    """
    Защищающее направленное заклинание, например создает препятствие в выбранной клетке
    """
    def __init__(self, name, energy, menu_image_id, sound, spell_range, obstacle_health):
        super().__init__(name, energy, menu_image_id, sound, spell_range)
        self.spell_type = 'defend_directed'
        self.obstacle_health = obstacle_health


class StateSpell(Spell):
    """
    Заклинание состояния. не имеет направления. Пример заклинани: увеличивает здоровье игрока
    """
    def __init__(self, name, energy, menu_image_id, sound):
        super().__init__(name, energy, menu_image_id, sound)
        self.spell_type = 'state'


class Projectile:
    def __init__(self, x, y, image_id, client_id):
        self.x = x
        self.y = y
        self.image_id = image_id
        self.client_id = client_id


