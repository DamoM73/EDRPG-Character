import edrpg
import tkinter as tk
from tkinter import ttk

FONT_LEVEL_1 = ('Arial',20)
FONT_LEVEL_2 = ('Arial',16)
FONT_LEVEL_3 = ('Arial',14)
FONT_LEVEL_4 = ('Arial',9)
BG_COLOUR_1 = 'white smoke'
BG_COLOUR_2 = 'white'




class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Elite Dangerous RPG Character Generator")
        self.geometry("1368x912")
        self.build_tabs(self)
        self.build_create_tab(self.create_tab)

        # CREATE STYLES
        style = ttk.Style()
        # Frames
        style.configure('Default.TFrame', background = 'white',bd=1)
        style.configure('Alt1.TFrame', background = 'wheat1',bd=1)
        # Labels
        style.configure('Level1.TLabel', background ='white',foreground='black',font=('Arial',20))
        style.configure('Level2.TLabel', background ='wheat1',foreground='black',font=('Arial',16))
        style.configure('Level3.TLabel', background ='wheat1',foreground='black',font=('Arial',14))
        style.configure('Level4.TLabel', background ='wheat1',foreground='black',font=('Arial',12))
        style.configure('Level5.TLabel', background ='wheat1',foreground='black',font=('Arial',9))
        # Entry 
        style.configure('Level3.TEntry', background ='wheat1',foreground='black',font=('Arial',14))
        # Button
        style.configure('Level3.TButton', font=('Arial',12))
        # Combox
        style.configure('Level3.TCombobox', font=('Arial',12))

    def build_tabs(self,container):
        ''' Builds the different tabs'''
        # Creating tabs
        self.tab_control = ttk.Notebook(container)
        # Create tab
        self.create_tab = ttk.Frame(self.tab_control, style='Alt1.TFrame')
        self.tab_control.add(self.create_tab, text = '     Create      ')
        # Character tab
        self.char_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.char_tab, text = '    Character    ', state='disabled')
        # Ship tab
        self.ship_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.ship_tab, text = '      Ship       ', state='disabled')
        # Vehicle tab
        self.vehc_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.vehc_tab, text = '    Vehicle     ', state='disabled')
        # Personal Combat tab
        self.per_com_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.per_com_tab, text = ' Personal Combat ', state='disabled')
        # Ship Combat tab
        self.ship_com_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.ship_com_tab, text = '   Ship Combat   ', state='disabled')
        # Vehicle Combat tab
        self.veh_com_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.veh_com_tab, text = ' Vehicle Combat  ', state='disabled')
        # Notes tab
        self.notes_tab = ttk.Frame(self.tab_control, style='Default.TFrame')
        self.tab_control.add(self.notes_tab, text = '      Notes       ')
        # Pack tabs
        self.tab_control.pack(expan = 1, fill = "both")

    def build_create_tab(self,container):
        # Title and containers
        ttk.Label(container,text='Character Creation',style='Level1.TLabel',width=16,anchor=tk.W)\
            .grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)

        # Name container        
        self.name_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.name_fr.grid(row=1,column=0,sticky=tk.W+tk.E,padx=5,pady=5)
        self.create_name(self.name_fr)

        # Background container
        self.backgrounds_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.backgrounds_fr.grid(row=2,column=0,sticky=tk.W+tk.E,padx=5,pady=5)
        self.select_backgrounds(self.backgrounds_fr)

        self.enhancements_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.enhancements_fr.grid(row=3,column=0)

        self.stats_fr = ttk.Frame(container,style='Default.TFrame')
        self.stats_fr.grid(row=4,column=0,columnspan=2)

        
    def create_name(self,container):
        ttk.Label(container,text='Step 1: Enter a name',style='Level2.TLabel')\
            .grid(row=0,column=0,columnspan=3, sticky=tk.W)
        ttk.Label(container,text='Character name',style='Level3.TLabel',width=13)\
            .grid(row=1,column=0)
        self.char_name_ent = ttk.Entry(container,width=28,font=FONT_LEVEL_3)
        self.char_name_ent.grid(row=1,column=1, padx=5)
        self.char_name_btn= ttk.Button(container,text='Commit',style='Level3.TButton',command=self.commit_name)
        self.char_name_btn.grid(row=1,column=2)

    def select_backgrounds(self,container):
        # Write Title
        ttk.Label(container,text='Step 2: Select Backgrounds',style='Level2.TLabel')\
            .grid(row=0,column=0,columnspan=2,sticky=tk.W)
        # create list of background names
        self.bg_options = ['None']
        for bg in edrpg.BACKGROUNDS:
            self.bg_options.append(bg.name)

        # background combo boxes
        ttk.Label(container,text="Background 1",style='Level3.TLabel', width=13)\
            .grid(row=1,column=0)
        self.bg_1_combo = ttk.Combobox(container, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_1_combo['values'] = self.bg_options
        self.bg_1_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_1_combo.grid(row=1,column=1,pady=5,padx=5)
        self.bg_1_combo.current(43)

        ttk.Label(container,text="Background 2",style='Level3.TLabel',width=13)\
            .grid(row=2,column=0)
        self.bg_2_combo = ttk.Combobox(container, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_2_combo['values'] = self.bg_options
        self.bg_2_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_2_combo.grid(row=2,column=1,pady=5,padx=5)

        ttk.Label(container,text="Background 3",style='Level3.TLabel',width=13)\
            .grid(row=3,column=0)
        self.bg_3_combo = ttk.Combobox(container, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_3_combo['values'] = self.bg_options
        self.bg_3_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_3_combo.grid(row=3,column=1,pady=5,padx=5)

        ttk.Label(container,text="Background 4",style='Level3.TLabel',width=13)\
            .grid(row=4,column=0)
        self.bg_4_combo = ttk.Combobox(container, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_4_combo['values'] = self.bg_options
        self.bg_4_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_4_combo.grid(row=4,column=1,pady=5,padx=5)

        ttk.Label(container,text="Background 5",style='Level3.TLabel',width=13)\
            .grid(row=5,column=0)
        self.bg_5_combo = ttk.Combobox(container, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_5_combo['values'] = self.bg_options
        self.bg_5_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_5_combo.grid(row=5,column=1,pady=5,padx=5)

    def commit_name(self):
        character.name = self.char_name_ent.get()
        print(character.name)

    def commit_background(self,event):
        pass






# ----- MAIN PROGRAM -----
if __name__ == '__main__':
    character = edrpg.Character()
    root = Root()
    root.mainloop()