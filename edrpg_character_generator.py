import edrpg
import tkinter as tk
from tkinter import ttk

class Root(tk.Tk):
    
    def __init__(self):
        super(Root,self).__init__()
        self.title("Elite Dangerous RPG Character Generator")
        self.geometry("1368x912")
        #self.state("zoomed")

        # Creating styles
        s = ttk.Style()
        s.configure('My.TFrame', background = 'white')
        self.font_level_1 = ('Arial',20)
        self.font_level_2 = ('Arial',16)
        self.font_level_3 = ('Arial',14)
        self.bg_colour_1 = 'white smoke'

        # Setting up tabs
        self.tab_control = ttk.Notebook(self)
        
        # Create tab
        self.create_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.create_tab, text = '     Create      ')
        # Character tab
        self.char_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.char_tab, text = '    Character    ', state='disabled')
        # Ship tab
        self.ship_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.ship_tab, text = '      Ship       ', state='disabled')
        # Vehicle tab
        self.vehc_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.vehc_tab, text = '    Vehicle     ', state='disabled')
        # Personal Combat tab
        self.per_com_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.per_com_tab, text = ' Personal Combat ', state='disabled')
        # Ship Combat tab
        self.ship_com_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.ship_com_tab, text = '   Ship Combat   ', state='disabled')
        # Vehicle Combat tab
        self.veh_com_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.veh_com_tab, text = ' Vehicle Combat  ', state='disabled')
        # Notes tab
        self.notes_tab = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(self.notes_tab, text = '      Notes       ')
        # Pack tabs
        self.tab_control.pack(expan = 1, fill = "both")

        # CREATE TAB Content
        # Title
        tk.Label(self.create_tab,text = 'Character Creation', font=(self.font_level_1), pady = 10, bg='white').pack()
        self.create_cont = tk.Frame(self.create_tab,bg=self.bg_colour_1)
        self.create_cont.pack(fill=tk.BOTH, padx=5,pady=5)
        # Name
        tk.Label(self.create_cont, text = 'Step 1: Choose a name', bg=self.bg_colour_1, font=self.font_level_2).grid(row=0, column=0, columnspan=3)
        tk.Label(self.create_cont, text='Character name', font=self.font_level_3, bg=self.bg_colour_1,padx=5, pady=5).grid(row=1, column=0)
        self.char_name_ent = tk.Entry(self.create_cont, width=30, font=self.font_level_3)
        self.char_name_ent.grid(row=1, column=1)
        self.char_name_btn = tk.Button(self.create_cont,text='Proceed',width=10)
        self.char_name_btn.grid(row=1,column=2)
        # Backgrounds
        tk.Label(self.create_cont,text='Step 2: Select Backgrounds', font=self.font_level_2, bg=self.bg_colour_1).\
            grid(row=2, column=0, columnspan=3)
        self.bg_options = []
        for bg in edrpg.BACKGROUNDS:
            self.bg_options.append(bg.name)
        tk.Label(self.create_cont,text="Background 1", font=self.font_level_3, bg=self.bg_colour_1).\
            grid(row=3,column=0)
        self.bg_1_combo = ttk.Combobox(self.create_cont, width=37,font=self.font_level_3)
        self.bg_1_combo['values'] = self.bg_options
        self.bg_1_combo.grid(row=3,column=1,columnspan=2)
        

        
        
        





if __name__ == '__main__':
    characters = []
    root = Root()
    root.mainloop() 