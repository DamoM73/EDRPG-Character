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
        #self.state("zoomed")

        # Creating styles
        s = ttk.Style()
        s.configure('My.TFrame', background = 'white')
        
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

        # CREATE TABS CONTENT
        # Title
        tk.Label(self.create_tab,text='Character Creation',font=(FONT_LEVEL_1),pady=10,bg='white',width=15,anchor=tk.W).pack()
        self.create_cont = tk.Frame(self.create_tab,bg=BG_COLOUR_1)
        self.create_cont.pack(fill=tk.BOTH,pady=5,side=tk.TOP)
        
        # Name
        label_2(self.create_cont,'Step 1: Choose a name',0,0,3)
        label_3(self.create_cont,'Character name',1,0,13,1)
        self.char_name_ent = tk.Entry(self.create_cont, width=30, font=FONT_LEVEL_3)
        self.char_name_ent.grid(row=1, column=1)
        self.char_name_btn = tk.Button(self.create_cont,text='Commit',width=10,command=self.commit_name)
        self.char_name_btn.grid(row=1,column=2)
        
        # Backgrounds
        label_2(self.create_cont,'Step 2: Select Backgrounds',2,0,3)
        self.bg_options = ['None']
        for bg in edrpg.BACKGROUNDS:
            self.bg_options.append(bg.name)
        
        label_3(self.create_cont,"Background 1",3,0,13,1)
        self.bg_1_combo = ttk.Combobox(self.create_cont, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_1_combo['values'] = self.bg_options
        self.bg_1_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_1_combo.grid(row=3,column=1,columnspan=2,pady=5)
        self.bg_1_combo.current(43)
        
        label_3(self.create_cont,"Background 2",4,0,13,1)
        self.bg_2_combo = ttk.Combobox(self.create_cont, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_2_combo['values'] = self.bg_options
        self.bg_2_combo.set(self.bg_options[0])
        self.bg_2_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_2_combo.grid(row=4,column=1,columnspan=2,pady=5)
        
        label_3(self.create_cont,"Background 3",5,0,13,1)
        self.bg_3_combo = ttk.Combobox(self.create_cont, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_3_combo['values'] = self.bg_options
        self.bg_3_combo.set(self.bg_options[0])
        self.bg_3_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_3_combo.grid(row=5,column=1,columnspan=2,pady=5)
        

        label_3(self.create_cont,"Background 4",6,0,13,1)
        self.bg_4_combo = ttk.Combobox(self.create_cont, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_4_combo['values'] = self.bg_options
        self.bg_4_combo.set(self.bg_options[0])
        self.bg_4_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_4_combo.grid(row=6,column=1,columnspan=2,pady=5)

        label_3(self.create_cont,"Background 5",7,0,13,1)
        self.bg_5_combo = ttk.Combobox(self.create_cont, width=37,font=FONT_LEVEL_3,state="readonly")
        self.bg_5_combo['values'] = self.bg_options
        self.bg_5_combo.set(self.bg_options[0])
        self.bg_5_combo.bind("<<ComboboxSelected>>",self.commit_background)
        self.bg_5_combo.grid(row=7,column=1,columnspan=2,pady=5)

        self.background_warning = tk.Label(self.create_cont,text="Warning! Too many backgrounds",font=FONT_LEVEL_3,bg="RED")
                
        # Enhancements
        label_2(self.create_cont,'Step 3:Enhancements',9,0,3)
        self.enhance_options = []
        for enh in edrpg.ENHANCEMENTS:
            self.enhance_options.append(enh.name)
        
        # Character Stats
        self.stats_cont = tk.Frame(self.create_tab,bg=BG_COLOUR_2)
        self.stats_cont.pack(fill=tk.BOTH,pady=5,side=tk.BOTTOM)
        self.display_stats(self.stats_cont) 

    def commit_name(self):
        characters[current_char].name = self.char_name_ent.get()
        print(characters[current_char].name)

    def commit_background(self,event):
        # reset the skills values
        for item in vars(characters[current_char]).items():
            if isinstance(item[1],edrpg.Skill):
                item[1].score = 10
        
        # get background slections
        backgrounds_selected  = []  
        backgrounds_selected.append(self.bg_1_combo.get())
        backgrounds_selected.append(self.bg_2_combo.get())
        backgrounds_selected.append(self.bg_3_combo.get())
        backgrounds_selected.append(self.bg_4_combo.get())
        backgrounds_selected.append(self.bg_5_combo.get())
        #print(backgrounds_selected)
        
        # write backgrounds to character
        index = 0
        for bg_name in backgrounds_selected:
            for bg_obj in edrpg.BACKGROUNDS:
                if bg_name == bg_obj.name:
                    characters[current_char].backgrounds[index] = bg_obj
                elif bg_name == "None":
                    characters[current_char].backgrounds[index] = ""
            index += 1
        bg_cost = 0
        
        # make calucations
        for bg_obj in characters[current_char].backgrounds:
            if isinstance(bg_obj,edrpg.Background):
                bg_cost += bg_obj.cost
                bg_obj.calculate_scores(characters[current_char])

        if bg_cost > 5:
            self.background_warning.grid(row=8,column=1)
        else:
            self.background_warning.grid_remove()

        self.display_stats(self.stats_cont) 
 
    def display_stats(self,container):
        stat_list = []
        for item in vars(characters[current_char]).items():
            if isinstance(item[1],edrpg.Skill):
                stat_list.append((item[1].name, item[1].cat, item[1].score))    
        
        label_2_alt(container,"Character Statistics",0,0,2)
        self.stats_warning= tk.Label(container,text="Stats exceeding Skill Cap",font=FONT_LEVEL_3,bg="RED")
        
        self.write_stats(container,stat_list,1)

    def write_stats(self,container,stats,row):
        cat_list=("Personal Combat","Intelligence","Social Skills","Vehicle Skills","Espionage")
        col=0
        stats_over = False
        for cat in cat_list:
            label_3_alt(container,cat,row,col,13,2)
            start_row = row+1
            for stat in stats:
                if stat[1] == cat[0]:
                    name = label_4_alt(container,stat[0],start_row,col,20)
                    score = label_4_alt(container,stat[2],start_row,col+1,5)
                    start_row += 1
                if stat[2] > characters[current_char].skill_cap:
                    stats_over = True
                               
            col += 2
        if stats_over:
            self.stats_warning.grid(row=0,column=2)
        else:
            self.stats_warning.config(bg=BG_COLOUR_2,fg=BG_COLOUR_2)
            self.stats_warning.grid(row=0,column=2)
            

class label_2:
    def __init__(self,container,text,row,col,col_span):
        tk.Label(container,text=text,bg=BG_COLOUR_1,font=FONT_LEVEL_2,height=1,anchor=tk.S)\
            .grid(row=row, column=col,columnspan=col_span)

class label_2_alt:
    def __init__(self,container,text,row,col,col_span):
        tk.Label(container,text=text,bg=BG_COLOUR_2,font=FONT_LEVEL_2,height=1,anchor=tk.S)\
            .grid(row=row, column=col,columnspan=col_span)

class label_3:
    def __init__(self,container,text,row,col,width,colspan):
        tk.Label(container,text=text,font=FONT_LEVEL_3,bg=BG_COLOUR_1,width=width,anchor=tk.W).\
            grid(row=row,column=col,columnspan=colspan,sticky=tk.W)

class label_3_alt:
    def __init__(self,container,text,row,col,width,colspan):
        tk.Label(container,text=text,font=FONT_LEVEL_3,bg=BG_COLOUR_2,width=width,anchor=tk.W).\
            grid(row=row,column=col,columnspan=colspan,sticky=tk.W)

class label_4:
    def __init__(self,container,text,row,col,width):
        tk.Label(container,text=text,font=FONT_LEVEL_4,bg=BG_COLOUR_1,width=width,anchor=tk.W).\
            grid(row=row,column=col)

class label_4_alt:
    def __init__(self,container,text,row,col,width):
        tk.Label(container,text=text,font=FONT_LEVEL_4,bg=BG_COLOUR_2,width=width,anchor=tk.W).\
            grid(row=row,column=col)



if __name__ == '__main__':
    characters = []
    current_char = 0
    characters.append(edrpg.Character())
    root = Root()
    root.mainloop() 