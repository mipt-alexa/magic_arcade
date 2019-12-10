from numpy import sign
import Spell_classes
from BattleField_class import Obstacle

BASIC_HEALTH = 100
BASIC_ENERGY = 100
STEP_ENERGY = 20
# -*- coding: utf-8 -*-
"""
Класс маг, класс персонажа, которым управляет игрок
"""


def vm(x1, y1, x2, y2):
    """
    Вектороное произведение vector_multiplication
    """
    return x1 * y2 - x2 * y1


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class Mage:
    def __init__(self, x, y, client_id, health=BASIC_HEALTH, energy=BASIC_ENERGY):
        self.type = 'Mage'
        self.x = x
        self.y = y
        self.health = health
        self.energy = energy
        self.client_id = client_id
        self.image_id = None

    def move(self, dx, dy):
        if self.energy >= STEP_ENERGY:
            self.x += dx
            self.y += dy
            self.energy -= STEP_ENERGY

    def check_move(self, click_x, click_y, obstacles, another_mage):
        if (abs(click_x - self.x) == 1 and abs(click_y - self.y) == 0) or (
                abs(click_x - self.x) == 0 and abs(click_y - self.y) == 1):
            if obstacles[click_y][click_x] is None and not (click_x == another_mage.x and click_y == another_mage.y):
                return True
            else:
                return False
        else:
            return False

    def check_spell(self, spell, obstacles=None, obj=None, mage_2=None):
        """
        метод проверяет, может ли маг вызвать заклинание.
        возвращает True, если да и False, если нет
        """
        if spell.spell_type == 'state':
            if self.energy >= spell.energy:
                return True
            else:
                return False

        elif spell.spell_type == 'defend_directed':
            if (obj.x == mage_2.x and obj.y == mage_2.y) or obstacles[obj.y][obj.x] is not None or self.energy < spell.energy:
                return False
            else:
                if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= spell.spell_range ** 2:
                    return True
                else:
                    return False
        elif spell.spell_type == 'attack_directed':
            flag = True
            if not (spell.destination == obj.type or spell.destination == 'Both'):
                flag = False
            """
            Проверка на наличие препятствия между целью и стреляющим
            """
            print("Start_checking", len(obstacles), len(obstacles[0]))
            i1 = min(self.y, obj.y)
            i2 = max(self.y, obj.y)
            j1 = min(self.x, obj.x)
            j2 = max(self.x, obj.x)
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    if obstacles[i][j] is not None and not (i == obj.y and j == obj.x):
                        print(i, j)
                        vl = [obj.x - self.x, obj.y - self.y]
                        v1 = [j - 0.5 - self.x, i - 0.5 - self.y]
                        v2 = [j - 0.5 - self.x, i + 0.5 - self.y]
                        v3 = [j + 0.5 - self.x, i - 0.5 - self.y]
                        v4 = [j + 0.5 - self.x, i + 0.5 - self.y]
                        vm1 = vm(vl[0], vl[1], v1[0], v1[1])
                        vm2 = vm(vl[0], vl[1], v2[0], v2[1])
                        vm3 = vm(vl[0], vl[1], v3[0], v3[1])
                        vm4 = vm(vl[0], vl[1], v4[0], v4[1])
                        print(vm1, vm2, vm3, vm4)
                        if not (vm1 * vm2 * vm3 * vm4 != 0 and abs(sign(vm1) + sign(vm2) + sign(vm3) + sign(vm4)) == 4):
                            flag = False

            if flag and self.energy >= spell.energy:
                if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= spell.spell_range ** 2:
                    return True
                else:
                    return False
            else:
                return False

    def cast_spell(self, spell):
        """
        метод отвечает за изменение параметров мага, связанных с приминением заклинания spell
        :param spell:
        """
        self.energy -= spell.energy

    def catch_spell(self, spell):
        """
        метод отвечает за изменение параметров мага, связанных с попаданием по нему заклинания spell
        :param spell:
        """
        self.health -= spell.health_damage
        self.energy -= spell.energy_damage
