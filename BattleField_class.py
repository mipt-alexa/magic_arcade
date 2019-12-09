from Cells_classes import Cell, Obstacle


"""
Класс игрового поля. Хранит информацию о клетках поля и препятствиях, которые на них стоят.
"""


class BattleField:
    def __init__(self, width, height, id_giver):
        self.width = width
        self.height = height
        self.field = [[]]
        self.obstacles = [[]]
        for i in range(height):
            self.field.append([])
            for j in range(width):
                cell = Cell(id_giver.new_id())
                self.field[i].append(cell)
        for i in range(height):
            self.obstacles.append([])
            for j in range(width):
                obstacle = None
                self.obstacles[i].append(obstacle)

    def attack_obstacle(self, health_damage, x, y):
        """
        метод отвечает за поподание мага по препятствию
        """
        if self.obstacles[y][x].health <= health_damage:
            self.delete_obstacles(x, y)
            return True
        else:
            self.obstacles[y][x].health -= health_damage
            return False

    def delete_obstacle(self, x, y):
        """
        метод отвечает за удаление препятствия
        """
        self.obstacles[y][x] = None

    def creat_obstacle(self, x, y, id_giver, health):
        """
        метод отвечает за создание препятствия
        """
        self.obstacles[y][x] = Obstacle(id_giver.new_id(), health)