from tkinter import *


tk_object = Tk()
tk_object.title('Counting Seconds')
button = tk_object.Button(tk_object, text='Stop', width=25, command=tk_object.destroy)
button.pack()
tk_object.mainloop(5)
from tkcalendar import DateEntry
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()