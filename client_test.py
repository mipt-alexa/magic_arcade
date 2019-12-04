import tkinter as tk
import time
import connection as con
root = tk.Tk()


def message_catcher():
    con.read_message("server")
    root.after(message_catcher, 30)

message_catcher()