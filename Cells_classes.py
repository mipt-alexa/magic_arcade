OBSTACLE_BASIC_HEALTH = 20


class Cell:
    """
    класс клетка, пока не несет в себе какой-либо информации, что вероятно изменится в дальнейем.
    В зависимости от дальнейшей реализации может содержать id визуального объекта с ним связанного.
    """

    def __init__(self, client_id):
        self.type = 'Cell'
        self.client_id = client_id
        self.image_id = '1'
        pass


class Obstacle:
    """
    класс препятствия
    """

    def __init__(self, client_id, health=OBSTACLE_BASIC_HEALTH):
        self.client_id = client_id
        self.type = 'Obstacle'
        self.image_id = '2'
