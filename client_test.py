import tkinter as tk
import time
import connection as con
root = tk.Tk()


def message_catcher():
    l = con.read_message("client")
    s = ''
    if len(l) > 0:
        s = l[0]
    if s != '':
        print(s)
    root.after(30, message_catcher)


message_catcher()
root.mainloop()