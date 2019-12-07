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

    def move(self, dx, dy):
        if self.energy >= STEP_ENERGY:
            self.x += dx
            self.y += dy
            self.energy -= STEP_ENERGY

    def check_move(self, click_x, click_y):
        if (abs(click_x - self.x) == 1 and not abs(click_y - self.y) == 1) or (not abs(click_x - self.x) == 1 and abs(click_y - self.y) == 1):
            return True
        else:
            return False

    def check_spell(self, spell, battle_field=None, obj=None):
        """
        метод проверяет, может ли маг вызвать заклинание.
        возвращает True, если да и False, если нет
        :param spell:
        :param battle_field:
        :param obj:
        """
        if spell.spell_type == 'state':
            if self.energy >= spell.energy:
                return True
            else:
                return False
        elif spell.spell_type == 'directed':
            flag = True
            # TODO написать проверку того, что между заклинанием и целью нет других обЪектов
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
        self.energy -= spell.lenergy_damage
