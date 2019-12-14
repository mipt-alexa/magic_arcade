# !/usr/bin/python
# coding=utf-8
OBSTACLE_BASIC_HEALTH = 20


class Cell:
    """
    класс клетка, пока не несет в себе какой-либо информации, что вероятно изменится в дальнейем.
    В зависимости от дальнейшей реализации может содержать id визуального объекта с ним связанного.
    """

    def __init__(self, x, y, client_id):
        self.x = x
        self.y = y
        self.type = 'Cell'
        self.client_id = client_id
        self.image_id = 'floor'
        pass


class Obstacle:
    """
    класс препятствия
    """

    def __init__(self, x, y, client_id, health=OBSTACLE_BASIC_HEALTH):
        self.client_id = client_id
        self.type = 'Obstacle'
        self.image_id = 'wall'
        self.x = x
        self.y = y
        self.health = health

    def take_damage(self, health_damage):
        """
        метод отвечает за поподание мага по препятствию
        """
        self.health = max(0, self.health - health_damage)
        if self.health == 0:
            return True
        else:
            return False
