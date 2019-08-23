from tkinter import *
import edrpg

tasha = edrpg.Character()

stats=[]

for item in vars(tasha).items():
    #print(item[1],isinstance(item[1],edrpg.Skill))
    if isinstance(item[1],edrpg.Skill):
        stats.append((item[1].name, item[1].cat, item[1].score))
        
print(stats)