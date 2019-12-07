class Cell:
    """
    класс клетка, пока не несет в себе какой-либо информации, что вероятно изменится в дальнейем.
    В зависимости от дальнейшей реализации может содержать id визуального объекта с ним связанного.
    """
    def __init__(self, client_id):
        self.type = 'Cell'
        self.client_id = client_id
        pass
