import socket


PORT = 14900


def start_connection_server():
    print("начало настройки связи")
    socket_server = socket.socket()
    socket_server.bind( ("", PORT) )
    socket_server.listen(2)
    conn_1, addr_1 = socket_server.accept()
    conn_2, addr_2 = socket_server.accept()
    return [conn_1, conn_2]
    
    
def start_connection_client():
    print("Напишите host сервера")
    host = input()
    conn = socket.socket()
    conn.connect((host, 14900))
    conn.setblocking(True)
    return conn


def read_message(conn):  
    """
    Отвечает за чтение сообщения
    """
    try:
        conn.settimeout(0.04)
        message = conn.recv(100)
        message_decode = message.decode("utf-8")
        print("read " + message_decode)  #exp
    except Exception:
        message_decode = ''
    return message_decode


def write_message_client(conn, message):  
    """
    Отвечает за отправку сообщения клиентом серверу
    """
    message += " "
    for i in range(100 - len(message)):
        message += "/"
    print("write " + message)  #exp
    message_encode = message.encode("utf-8")
    conn.send(message_encode)
    
    
def write_message_server(conn_1, conn_2, message):  
    """
    Отвечает за отправку сообщения сервером обеим клиентам
    """
    message += " "
    for i in range(100 - len(message)):
        message += "/"
    print("write " + message)  #exp
    message_encode = message.encode("utf-8")
    conn_1.send(message_encode)
    conn_2.send(message_encode)
