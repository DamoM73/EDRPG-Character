import edrpg
import tkinter as tk
from tkinter import ttk

WIDTH=1368
HEIGHT=912

FONT_LEVEL_1 = ('Arial',20)
FONT_LEVEL_2 = ('Arial',16)
FONT_LEVEL_3 = ('Arial',14)
FONT_LEVEL_4 = ('Arial',12)
FONT_LEVEL_5 = ('Arial',9)
BG_COLOUR_1 = 'black'
FG_COLOUR_1 = 'dark orange2'
BG_COLOUR_2 = 'dark orange2'
FG_COLOUR_2 = 'black'


class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Elite Dangerous RPG Character Generator")
        self.geometry("{}x{}".format(WIDTH,HEIGHT))
        self.build_tabs(self)
        self.build_create_tab(self.create_tab)

        # CREATE STYLES
        style = ttk.Style()
        # Frames
        style.configure('Default.TFrame', background = BG_COLOUR_2)
        style.configure('Alt1.TFrame', background = BG_COLOUR_1)
        # Labels
        style.configure('Level1.TLabel', background =BG_COLOUR_2,foreground=FG_COLOUR_2,font=(FONT_LEVEL_1))
        style.configure('Level2.TLabel', background =BG_COLOUR_1,foreground=FG_COLOUR_1,font=(FONT_LEVEL_2))
        style.configure('Level3.TLabel', background =BG_COLOUR_1,foreground=FG_COLOUR_1,font=(FONT_LEVEL_3))
        style.configure('Level4.TLabel', background =BG_COLOUR_1,foreground=FG_COLOUR_1,font=(FONT_LEVEL_4))
        style.configure('Level5.TLabel', background =BG_COLOUR_1,foreground=FG_COLOUR_1,font=(FONT_LEVEL_5))
        style.configure('Level3_Warning.TLabel', background =BG_COLOUR_1,foreground='red',font=(FONT_LEVEL_3))
        # Entry 
        style.configure('Level3.TEntry', background =BG_COLOUR_1,foreground=FG_COLOUR_1,font=(FONT_LEVEL_3))
        # Button
        style.configure('Level3.TButton', font=(FONT_LEVEL_4))
        # Combox
        style.configure('Level3.TCombobox', font=(FONT_LEVEL_4))

    def build_tabs(self,container):
        ''' Builds the different tabs'''
        # Creating tabs
        self.tab_control = ttk.Notebook(container)
        # Create tab
        self.create_tab = ttk.Frame(self.tab_control, style='Alt1.TFrame',width=WIDTH,height=HEIGHT)
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
        ttk.Label(container,text='Character Creation',style='Level1.TLabel')\
            .grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)
        
        # Name container        
        self.name_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.name_fr.grid(row=1,column=0,sticky=tk.W+tk.E,padx=5,pady=5)
        self.create_name(self.name_fr)

        # Background container
        self.backgrounds_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.backgrounds_fr.grid(row=2,column=0,sticky=tk.W+tk.E,padx=5,pady=5)
        self.select_backgrounds(self.backgrounds_fr)

        # Enchancements container
        self.enhancements_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.enhancements_fr.grid(row=3,column=0)

        # Stats container
        self.stats_fr = ttk.Frame(container,style='Alt1.TFrame')
        self.stats_fr.grid(row=4,column=0,columnspan=2,sticky=tk.S,padx=5)
        self.display_stats(self.stats_fr)

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
        # Prepare warning
        self.back_warn_var = tk.StringVar()
        self.back_warn_var.set("")
        self.backgrounds_warning = ttk.Label(container,textvariable=self.back_warn_var,style='Level3_Warning.TLabel')\
            .grid(row=0,column=1,sticky=tk.E)
                
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
        # reset the skills values
        for item in vars(character).items():
            if isinstance(item[1],edrpg.Skill):
                item[1].score = 10

        # get background slections
        backgrounds_selected  = []  
        backgrounds_selected.append(self.bg_1_combo.get())
        backgrounds_selected.append(self.bg_2_combo.get())
        backgrounds_selected.append(self.bg_3_combo.get())
        backgrounds_selected.append(self.bg_4_combo.get())
        backgrounds_selected.append(self.bg_5_combo.get())

        # write backgrounds to character
        index = 0
        for bg_name in backgrounds_selected:
            for bg_obj in edrpg.BACKGROUNDS:
                if bg_name == bg_obj.name:
                    character.backgrounds[index] = bg_obj
                elif bg_name == "None":
                    character.backgrounds[index] = ""
            index += 1
        bg_cost = 0

        # make background skills calucations & write enhancements to character
        for bg_obj in character.backgrounds:
            if isinstance(bg_obj,edrpg.Background):
                bg_cost += bg_obj.cost
                bg_obj.calculate_scores(character)
        if bg_cost > 5:
            self.back_warn_var.set("Backgrounds exceed limit")
        else:
            self.back_warn_var.set("")
        
        # update character stats
        self.display_stats(self.stats_fr) 

    def display_stats(self,container):
        stat_list = []
        for item in vars(character).items():
            if isinstance(item[1],edrpg.Skill):
                stat_list.append((item[1].name, item[1].cat, item[1].score))    
        # display title
        ttk.Label(container,text="Character Statistics",style='Level2.TLabel')\
            .grid(row=0,column=0,columnspan=4,stick=tk.W)
        # prepare warning
        self.stat_warn_var = tk.StringVar()
        self.stat_warn_var.set("")
        self.stat_warning = ttk.Label(container,textvariable=self.stat_warn_var,style='Level3_Warning.TLabel')\
            .grid(row=0,column=6,columnspan=3,sticky=tk.E)
        self.write_stats(container,stat_list,1)

    def write_stats(self,container,stats,row):
        # set local variables
        cat_list=("Personal Combat","Intelligence","Social Skills","Vehicle Skills","Espionage")
        col=0
        stats_over = False
        
        # print each category heading
        for cat in cat_list:
            ttk.Label(container,text=cat,style='Level4.TLabel').grid(row=row,column=col,columnspan=2,sticky=tk.W)
            start_row = row+1
            # print skills for each category
            for stat in stats:
                if stat[1] == cat[0]:
                    ttk.Label(container,text=stat[0],style='Level5.TLabel',width=20)\
                        .grid(row=start_row,column=col)
                    ttk.Label(container,text=stat[2],style='Level5.TLabel',width=5)\
                        .grid(row=start_row,column=col+1)
                    start_row += 1
                if stat[2] > character.skill_cap:
                    stats_over = True
            col += 2
        # display warning if stats over
        if stats_over:
            self.stat_warn_var.set("Stats exceeding Skill Cap")
        else:
            self.stat_warn_var.set("")
        

# ----- MAIN PROGRAM -----
if __name__ == '__main__':
    character = edrpg.Character()
    root = Root()
    root.mainloop()