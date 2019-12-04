import tkinter as tk
import time
import connection as con
root = tk.Tk()


def message_catcher():
    print(con.read_message("client"))
    root.after(30, message_catcher)


message_catcher()
root.mainloop()