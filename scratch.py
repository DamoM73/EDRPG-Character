from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="red")

btn = ttk.Button(text="Sample")
btn.pack()

root.mainloop()