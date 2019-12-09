from numpy import sign
import Spell_classes
from BattleField_class import Obstacle

BASIC_HEALTH = 100
BASIC_ENERGY = 100
STEP_ENERGY = 20

"""
Класс маг, класс персонажа, которым управляет игрок
"""


def vm(x1, y1, x2, y2):
    """
    Вектороное произведение vector_multiplication
    """
    return x1 * y2 - x2 * y1


def ca(x1, y1, x2, y2):
    """
    Косинус угла между векторами cos_angle
    """
    return (x1 * y1 + x2 * y2) / ((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2)) ** 2


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
            if (obj.x == mage_2.x and obj.y == mage_2.y) or (type(obstacles[obj.x][obj.y]) == Obstacle):
                return False
            else:
                return True
        elif spell.spell_type == 'attack_directed':
            flag = True
            """
            Проверка на наличие препятствия между целью и стреляющим
            """
            dx = obj.x - self.x
            dy = obj.y - self.y
            k = 0
            for x in range(10):
                if k == 1:
                    break
                for y in range(10):
                    if (x == obj.x and y == obj.y) or (x == self.x and y == self.y):
                        continue
                    if ca(x - 0.5, y - 0.5, dx, dy) <= 0 and ca(x + 0.5, y - 0.5, dx, dy) <= 0 and ca(x + 0.5, y + 0.5,
                                                                                                      dx,
                                                                                                      dy) <= 0 and ca(
                            x - 0.5, y + 0.5, dx, dy) <= 0:
                        continue
                    condition_1 = vm(x - 0.5, y - 0.5, dx, dy) * vm(x - 0.5, y + 0.5, dx, dy) * vm(x + 0.5, y + 0.5, dx,
                                                                                                   dy) * vm(x + 0.5,
                                                                                                            y - 0.5, dx,
                                                                                                            dy) == 0
                    condition_2 = abs(
                        vm(x - 0.5, y - 0.5, dx, dy) + vm(x - 0.5, y + 0.5, dx, dy) + vm(x + 0.5, y + 0.5, dx, dy) + vm(
                            x + 0.5, y - 0.5, dx, dy)) == abs(vm(x - 0.5, y - 0.5, dx, dy)) + abs(
                        vm(x - 0.5, y + 0.5, dx, dy)) + abs(vm(x + 0.5, y + 0.5, dx, dy)) + abs(
                        vm(x + 0.5, y - 0.5, dx, dy))
                    if condition_1 or condition_2:
                        if type(obstacles[x][y]) == Obstacle:
                            flag = False
                            k = 1
                            break
            if flag and self.energy >= spell.energy:
                return True
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
