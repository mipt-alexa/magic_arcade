#! /usr/bin/env python
# -*- coding: utf-8 -*-
print("Запустить игру или присоединиться? (1 или 2)")
answer = input()
if answer == "1":
    import subprocess
    print("Напишите host сервера")
    host = input()
    file_host = open("host.txt", 'w', encoding='utf-8')
    file_host.write("{}".format(host))
    file_host.close()
    subprocess.Popen("python server.py", shell=True)
    subprocess.Popen("python client_main.py", shell=True)
else:
    import subprocess
    print("Напишите host сервера")
    host = input()
    file_host = open("host.txt", 'w', encoding='utf-8')
    file_host.write("{}".format(host))
    file_host.close()
    subprocess.call("python client_main.py", shell = True)