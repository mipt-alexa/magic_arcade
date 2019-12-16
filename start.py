
print("Запустить игру или присоединиться? (1 или 2)")
answer = input()
if answer == "1":
    import subprocess
    print("Напишите host сервера")
    host = input()
    file_host = open("host.txt", 'w', encoding = 'utf-8')
    file_host.write("{}".format(host))
    file_host.close()
    subprocess.Popen("python server.py")
    subprocess.Popen("python client_main.py")
else:
    import subprocess
    print("Напишите host сервера")
    host = input()
    file_host = open("host.txt", 'w', encoding = 'utf-8')
    file_host.write("{}".format(host))
    file_host.close()
    subprocess.call("python client_main.py")