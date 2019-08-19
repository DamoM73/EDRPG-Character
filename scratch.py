from tkinter import *
import edrpg

root = Tk()
root.geometry("300x200")

option_list = []
for bg in edrpg.BACKGROUNDS:
    option_list.append(bg.name)

print(option_list)

option_control = StringVar()
option_control.set = (option_list[0])
choice = OptionMenu(root, option_control, *option_list)
choice.pack()

root.mainloop()