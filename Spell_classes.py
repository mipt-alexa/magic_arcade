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
    """
    Класс направленного заклинания, которое применяется на некоторый объект (маг ил препятствие) или клетку
    """
    def __init__(self, name, energy, range):
        super().__init__(name, energy)
        self.range = range
        self.spell_type = 'directed'


class AttackDirectSpell(DirectSpell):
    """
    Направленное заклинание, наносящее урон
    """
    def __init__(self, name, energy, range, health_damage, energy_damage, destination):
        super().__init__(name, energy, range)
        self.destination = destination # тип объекта на который может быть направленно заклинание(Mage, Obstacle, Both)
        self.health_damage = health_damage
        self.energy_damage = energy_damage


class DefendDirectSpell(DirectSpell):
    """
    Защищающее направленное заклинание, например создает препятствие в выбранной клетке
    """
    pass


class StateSpell(Spell):
    """
    Заклинание состояния. не имеет направления. Пример заклинани: увеличивает здоровье игрока
    """
    def __init__(self, name, energy):
        super().__init__(name, energy)
        self.spell_type = 'state'




