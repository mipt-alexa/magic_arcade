from Cells_classes import Cell


"""
Класс игрового поля. Хранит информацию о клетках поля и препятствиях, которые на них стоят.
"""


class BattleField:
    def __init__(self, width, height, obstacles_number):
        self.width = width
        self.height = height
        self.field = [[]]
        self.obstacles = [[]]
        for i in range(height):
            self.field.append([])
            for j in range(width):
                cell = Cell()
                self.field[i].append(cell)
        for i in range(obstacles_number):
            pass