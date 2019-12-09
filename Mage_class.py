from numpy import sign
import Spell_classes
from BattleField_class import Obstacle


BASIC_HEALTH = 100
BASIC_ENERGY = 100
STEP_ENERGY = 20

"""
Класс маг, класс персонажа, которым управляет игрок
"""


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
        if (abs(click_x - self.x) == 1 and abs(click_y - self.y) == 0) or (abs(click_x - self.x) == 0 and abs(click_y - self.y) == 1):
            if obstacles[click_y][click_x] is None and not (click_x == another_mage.x and click_y == another_mage.y):
                return True
            else:
                return False
        else:
            return False

    def check_spell(self, spell, obstacles=None, obj=None):
        """
        метод проверяет, может ли маг вызвать заклинание.
        возвращает True, если да и False, если нет
        """
        if spell.spell_type == 'state':
            if self.energy >= spell.energy:
                return True
            else:
                return False
        elif spell.spell_type == 'attack_directed' or spell.spell_type == 'defend_directed':
            flag = True
            """
            Проверка того, есть ли между Mage и obj, на которое применяют магию препятствия
            """
            # Необходимо выполнить проверку этой части
            if obj.x - self.x == 0:
                for i in range(self.y, obj.y, 1):
                    if type(obstacles[self.x][i]) == Obstacle:
                        flag = False
                        break
            else:
                tg = (obj.y - self.y) / (obj.x - self.x)
                if tg == 1:
                    for i in range(self.y, obj.y, 1):
                        if type(obstacles[i][i]) == Obstacle:
                            flag = False
                            break
                else:
                    if tg * 0.5 > 0.5:
                        displacement = 0.5 + 0.5 / tg
                        turn = 'y'
                    else:
                        displacement = 0.5 + 0.5 * tg
                        turn = 'x'
                    x_pr = self.x
                    y_pr = self.y
                    while x_pr != obj.x or y_pr != obj.y:
                        """
                        Пробегаются все поля (переменные x_pr, y_pr), затрагиваемые линией выстрела и идет проверка на препятствия
                        """
                        if turn == 'x':
                            if type(obstacles[x_pr + sign(obj.x - self.x)][y_pr]) == Obstacle:
                                flag = False
                                break
                            x_pr += sign(obj.x - self.x)
                            displacement += tg
                            if displacement == 1:
                                if type(obstacles[x_pr][y_pr + sign(obj.y - self.y)]) == Obstacle:
                                    flag = False
                                    break
                                y_pr += sign(obj.y - self.y)
                                displacement = 0
                            elif displacement >= 1:
                                turn = 'y'
                                displacement = (1 - displacement) / tg
                        else:
                            if type(obstacles[x_pr][y_pr + sign(obj.y - self.y)]) == Obstacle:
                                flag = False
                                break
                            y_pr += sign(obj.y - self.y)
                            displacement += 1 / tg
                            if displacement == 1:
                                if type(obstacles[x_pr +  sign(obj.x - self.x)][y_pr]) == Obstacle:
                                    flag = False
                                    break
                                x_pr += sign(obj.x - self.x)
                                displacement = 0
                            elif displacement >= 1:
                                turn = 'x'
                                displacement = (1 - displacement) * tg
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