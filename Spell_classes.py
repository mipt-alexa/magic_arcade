"""
Данные классы являются неким конструктром заклинаний.
Сами саклинания будут создаваться как обЪекты этих классов с заданными параметрами.
Эти обЪекты будут храниться в отдельном словаре или даже файле с названием spell_book.
"""


class Spell:
    def __init__(self, name, energy):
        self.type = 'spell'
        self.energy = energy
        self.name = name


class DirectSpell(Spell):
    def __init__(self, range):
        super().__init__()
        self.range = range
        self.spell_type = 'directed'


class AttackDirectSpell(DirectSpell):
    def __init__(self, health_damage, energy_damage):
        super().__init__()
        self.health_damage = health_damage
        self.energy_damage = energy_damage

    def cast(self, mage, obj):
        if (mage.x - obj.x)**2 + (mage.y - obj.y)**2 <= self.range**2:
            obj.health -= self.health_damage
            obj.energy -= self.energy_damage


class DefendDirectSpell(DirectSpell):
    pass


class StateSpell(Spell):
    def __init__(self):
        super().__init__()
        self.spell_type = 'state'





