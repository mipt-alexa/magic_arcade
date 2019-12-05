import tkinter as tk
import time
import connection as con
root = tk.Tk()
i = 0


def message_sender():
    global i
    con.write_message("server", str(i))
    i += 1
    root.after(500, message_sender)


message_sender()
root.mainloop()