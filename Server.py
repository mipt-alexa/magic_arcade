import socket

"""
Класс отвечающий за взаимодействие двух игроков с Main_2_players
"""

# Константы связи сервера и клиентов
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
CONN = []
ADD = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

    
def staring_connection():
    """
    Отвечает за установки связи сервера и 1 игрока. Совершает проверку установки
    """

    s.listen(2)
    for i in [0, 1]:
        CONN[i], addr[i] = s.accept()
        with conn[i]:
            CONN[i].sendall('1')
            CONN[i].recv(1024)
    return [CONN, ADDR] 


def start_to_paint(width, height):
    for i in [0, 1]:
        with CONN[i]:
            CONN[i].sendall(' ')#FIXME: отправить width, height
            CONN[i].recv(1024)



