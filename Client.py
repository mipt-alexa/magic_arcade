import socket
import Vision

print('Напишите ваш хост') 
HOST = input()    # The remote host
PORT = 50007              # The same port as used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


staring_connection()
def staring_connection():
    data = s.recv(1024)
    s.sendall(data)
    

def start_to_paint():
    #TODO: принять с сервера width, height
    Vision.starting_paint(width, height)