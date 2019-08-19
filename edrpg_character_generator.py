import edrpg
import tkinter as tk
from tkinter import ttk

class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Elite Dangerous RPG Character Generator")
        self.geometry("1920x1080")


if __name__ == '__main__':
    root = Root()
    root.mainloop()