class Character:
    def __init__(self, name, age, height, weight):
        # cosmetics
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
        # general
        self.rank_index = 0
        self.rank_pts = 0
        self.rank_name = RANKS[self.rank_index].name
        self.skillcap = RANKS[self.rank_index].skill_cap
        self.endurance = RANKS[self.rank_index].end
        self.karma = RANKS[self.rank_index].karma_pts
        self.backgrounds = []
        self.enhancements = []
        self.karam_caps = []
        self.carried_weap = []
        self.clothing = []
        self.pack = []
        self.ship_inv = []
        self.cash = Money(1000,0,0)
        self.ships = []
        
        # Personal Combat Skills
        self.dodge = Skill("Dodge","P")
        self.eng_weap = Skill("Energy Weapons", "P")
        self.fight = Skill("Fighting", "P")
        self.grenade = Skill("Grenade", "P")
        self.hvy_weap = Skill("Heavy Weapons", "P")
        self.kin_weap = Skill("Kinetic Weapons", "P")
        self.mel_weap = Skill("Melee Weapon", "P")
        self.parry = Skill("Parry", "P")
        
        # Intelligence Skills
        self.comp = Skill("Computer", "I")
        self.cult_law = Skill("Cullture & Law", "I")
        self.cyber = Skill("Cyber", "I")
        self.med = Skill("Medicine", "I")
        self.plant_know = Skill("Planetary Knowledge", "I")
        self.sci = Skill("Science", "I")
        self.tact = Skill("Tactics", "I")
        self.trade = Skill("Trading", "I")

        # Social Skills
        self.bargin = Skill("Bargin", "S")
        self.bluff = Skill("Bluff", "S")
        self.charm = Skill("Charm", "S")
        self.dip = Skill("Diplomacy", "S")
        self.gambling = Skill("Gambling", "S")
        self.insight = Skill("Insight", "S")
        self.intim = Skill("Intimidate", "S")
        self.strwise = Skill("Streewise","S")

        # Vehicle Skills
        self.nav = Skill("Navigation", "V")
        self.repair = Skill("Repair", "V")
        self.ship_plt = Skill("Spaceship Piloting", "V")
        self.ship_weap = Skill("Spaceship Weapons", "V")
        self.sys = Skill("Systems", "V")
        self.veh_plt = Skill("Vehicle Piloting", "V")
        self.veh_weap = Skill("Vehicle Weapons", "V")

        # Espionage
        self.athlet = Skill("Athletics", "E")
        self.perc = Skill("Perception", "E")
        self.sec = Skill("Security", "E")
        self.slt_o_hand = Skill("Slight of Hand", "E")
        self.sealth = Skill("Stealth", "E")
        self.surv = Skill("Survival", "E")


class Skill:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
        self.score = 10
        self.bonus = self.score // 10
        self.used = False

    def update(self, amt, skillcap):
        self.score += amt
        if self.score > skillcap:
            self.bonus = skillcap // 10
        else:
            self.bonus = self.score // 10


class Rank:
    def __init__(self, name, points, skill_cap, karma_pts, karma_caps, end):
        self.name = name
        self.points = points
        self.skill_cap = skill_cap
        self.karma_pts = karma_pts
        self.karam_caps = karma_caps
        self.end = end


class Money:
    def __init__(self, cred, micro_creds, units):
        self.cr = cred
        self.mcr = micro_creds
        self.u = units

    def display(self):
        return("{}Cr {}Mcr {}U".format(self.cr, self.mcr, self.u))

    def update(self, cr, mcr, u):
        # add amounts
        self.cr += cr
        self.mcr += mcr
        self.u += u
        
        # convert
        if self.u < 0:
            while self.u < 0:
                self.mcr -= 1
                self.u += 10000
        elif self.u >= 10000:
            self.mcr += self.u // 10000 
            self.u = self.u % 10000

        if self.mcr < 0:
            while self.mcr < 0:
                self.cr -= 1
                self.mcr += 100
        elif self.mcr >= 100:
            self.cr += self.mcr // 100 
            self.mcr = self.mcr % 100
        

class Ship:
    def __init__(self, ship_model, ship_name, pilot):
        # cosmetic
        self.model = ship_model
        self.name = ship_name
        self.size = SHIPS[self.model][0]
        self.manufacture = SHIPS[self.model][1]
        self.landing_pad = SHIPS[self.model][2]
        
        # general
        self.crew = SHIPS[self.model][3]
        self.passengers = SHIPS[self.model][4]
        self.agility = SHIPS[self.model][5]
        self.spd = SHIPS[self.model][6]
        self.range = SHIPS[self.model][7]
        self.fuel = 0
        self.hull = SHIPS[self.model][9]
        self.shields = 0
        self.shield_recharge = 5

        # combat stats
        self.initiative = pilot.tact.bonus
        self.defence = self.agility + pilot.ship_plt.bonus
        self.dogfight = self.defence
        self.pursuit = self.spd + pilot.ship_plt.bonus // 2

        # creating slots
        self.bh_slot = Slot(0)
        self.pp_slot = Slot(SHIPS[self.model][10])
        self.th_slot = Slot(SHIPS[self.model][11])
        self.fsd_slot = Slot(SHIPS[self.model][12])
        self.ls_slot = Slot(SHIPS[self.model][13])
        self.pd_size = Slot(SHIPS[self.model][14])
        self.s_size = Slot(SHIPS[self.model][15])
        self.f_size = Slot(SHIPS[self.model][16])
        self.weapon_slots = []
        self.ulity_mounts = []
        self.internal_slots = []
        self.military_slots = []
        self.crew = []

        # allocating weapon slots
        slots = SHIPS[self.model][20:24]
        options = [1, 2, 3, 4]
        for i in range(4):
            for j in range(slots[i]):
                self.weapon_slots.append(Slot(options[i]))
        
        # allocating utility slots
        for i in range(SHIPS[self.model][24]):
            self.ulity_mounts.append(Slot("Util"))
        
        # allocating internal slots
        slots= SHIPS[self.model][25:33]
        options = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(8):
            for j in range(slots[i]):
                self.internal_slots.append(Slot(options[i]))

        # allocating military slots
        slots= SHIPS[self.model][33:41]
        options = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(8):
            for j in range(slots[i]):
                self.military_slots.append(Slot(options[i]))

        # allocating crew slots
        for i in range(SHIPS[self.model][3]):
            self.ulity_mounts.append(Slot("Crew"))
        

class Slot:
    def __init__(self, size):
        self.size = size
        self.content = Empty()


class Empty:
    def __init__(self):
        self.name = "Empty"


class Ship_weapon:
    def __init__(self, code):
        self.name(SHIPS[0])
        self.size(SHIPS[1])
        self.str(SHIPS[2])
        self.pwr(SHIPS[3])
        self.to_hit(SHIPS[4])
        self.sld_sml(SHIPS[5])
        self.sld_med(SHIPS[6])
        self.sld_lrg(SHIPS[7])
        self.amr_sml(SHIPS[8])
        self.arm_med(SHIPS[9])
        self.arm_lrg(SHIPS[10])
        self.burst(SHIPS[11])
        self.ammo(SHIPS[12])
        self.cost(SHIPS[13])
        self.effect(SHIPS[14])
        self.effect_amt(SHIPS[15])
        self.notes(SHIPS[16])


class Utility:
    def __init__(self, code):
        self.name(UTILITIES[0])
        self.size(UTILITIES[1])
        self.str(UTILITIES[2])
        self.pwr(UTILITIES[3])
        self.model(UTILITIES[4])
        self.desr(UTILITIES[5])
        self.ammo(UTILITIES[6])
        self.cost(UTILITIES[7])
        self.effect(UTILITIES[8])
        self.effect_amt(UTILITIES[9])


# Constants 
RANKS = [Rank("Harmless",0,40,10,3,20), Rank("Mostly Harmless", 8, 50, 11, 4, 25),\
    Rank("Novice", 20, 55, 12, 5, 30), Rank("Competent", 40, 60, 13, 6, 35),\
    Rank("Expert", 70, 65, 14, 7, 40), Rank("Master", 100, 70, 15, 8, 45),\
    Rank("Dangerous", 150, 80, 16, 9, 50), Rank("Deadly", 200, 90, 17, 10, 55),\
    Rank("Elite", 300, 100, 18, 11, 60)]

SHIPS = {"Adder": ["Small", "Zorgon Peterson", "Small",2,1,8,6,"Exp",8,76,40000,35120,79030,3,3,3,1,2,3,3,2,1,0,0,2,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Alliance Challenger": ["Medium", "Lakon", "Medium",0,0,0,0,"Std",16,0,28041035,6803170,15307134,6,6,5,5,6,4,4,3,3,1,0,4,1,2,2,0,0,2,0,0,0,0,0,3,0,0,0,0],\
    "Alliance Chieftain": ["Medium", "Lakon", "Medium",0,0,0,0,"Std",16,0,18182883,6803170,15307134,6,6,5,5,6,4,4,3,1,2,0,4,1,2,0,1,1,1,0,0,0,0,0,3,0,0,0,0],\
    "Alliance Crusader": ["Medium", "Lakon", "Medium",0,0,0,0,"Std",16,0,22866341,6803170,15307134,6,6,5,5,6,4,4,3,2,1,0,4,1,2,2,0,1,1,0,0,0,0,0,3,0,0,0,0],\
    "Anaconda": ["Large", "Faulcon DeLacy", "Large",8,12,2,2,"Exp",32,950,141889930,58787780,132272510,8,7,6,5,8,8,5,2,2,3,1,8,1,1,0,3,3,3,1,0,0,0,0,0,1,0,0,0],\
    "Asp Explorer": ["Medium", "Lakon", "Medium",2,4,6,7,"Exp",32,285,6135660,2664460,5995040,5,5,5,4,4,5,5,4,2,0,0,4,1,2,3,0,1,1,0,0,0,0,0,0,0,0,0,0],\
    "Asp Scout": ["Medium", "Lakon", "Medium",2,2,8,5,"Exp",16,250,3818240,1584460,3565040,4,4,4,3,4,4,4,2,2,0,0,2,1,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0],\
    "Beluga Liner": ["Large", "Saud Kruger", "Large",0,0,0,0,"Std",128,0,79654610,33813120,76079500,6,7,7,8,6,5,7,0,5,0,0,6,1,0,4,1,2,4,0,0,0,0,0,0,0,0,0,0],\
    "Boa": ["Huge", "Faulcon DeLacy", "None",14,20,1,1,"Std",128,2000,350000000,135000000,370000000,8,8,8,8,8,8,7,0,2,4,2,8,0,1,0,0,2,3,1,4,0,0,0,0,0,0,0,0],\
    "Cobra Mk III": ["Small","Faulcon DeLacy","Small",2,2,7,10,"Std",16,100,205800,151890,341750,4,4,4,3,3,3,4,2,2,0,0,2,2,3,0,3,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Cobra Mk IV": ["Small","Faulcon DeLacy","Small",2,2,3,4,"Std",16,100,603740,305890,688250,4,4,4,3,3,3,4,3,2,0,0,2,2,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Diamondback Explorer": ["Small","Lakon","Small",1,1,6,6,"Exp",32,120,1635700,800000,1800000,4,4,5,3,4,3,5,0,2,1,0,4,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Diamondback Scout": ["Small","Lakon","Small",1,1,8,9,"Exp",16,100,461340,225700,507900,4,4,4,2,3,2,4,2,2,0,0,4,2,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Dolphin": ["Small","Saud Kruger","Small",0,0,0,0,"Std",16,0,1115330,534940,1203600,4,5,4,4,3,3,4,2,0,0,0,3,2,3,1,2,1,0,0,0,0,0,0,0,0,0,0,0],\
    "Eagle": ["Small","Core Dynamics","Small",1,0,10,7,"Std",4,35,10440,26880,90050,2,3,3,1,2,2,2,3,0,0,0,1,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Federal Assault Ship": ["Medium","Core Dynamics","Medium",2,6,6,7,"Std",16,360,19072000,7925680,17832780,6,6,5,5,6,4,4,0,2,2,0,4,1,2,1,3,2,0,0,0,0,0,0,0,0,0,0,0],\
    "Federal Corvette": ["Large","Core Dynamics","Large",8,12,2,5,"Std",32,660,182589570,75187790,169172510,8,7,6,5,8,8,5,2,2,1,2,8,1,0,1,2,2,2,3,0,0,0,0,0,2,0,0,0],\
    "Federal Dropship": ["Medium","Core Dynamics","Medium",2,8,2,8,"Std",16,360,13469990,5725680,12882780,6,6,5,5,6,4,4,0,4,1,0,4,1,1,2,1,2,1,0,0,0,0,0,2,0,0,0,0],\
    "Federal Gunship": ["Medium","Core Dynamics","Medium",2,3,2,4,"Std",16,420,34774790,14325690,32232790,6,6,5,5,7,5,4,2,4,1,0,4,1,2,0,3,1,2,0,0,0,0,0,0,0,0,0,0],\
    "Fer-de-Lance": ["Medium","Zorgon Peterson","Medium",2,6,6,8,"Std",8,300,51232230,20626820,46410340,6,5,4,4,6,4,3,0,4,0,1,6,2,1,0,2,1,0,0,0,0,0,0,0,0,0,0,0],\
    "Hauler": ["Small","Zorgon Peterson","Small",1,1,6,5,"Exp",4,45,29790,42180,185050,2,2,2,1,1,1,2,1,0,0,0,2,3,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Imperial Clipper": ["Large","Gutamaya","Large",4,8,5,9,"Std",16,490,21077780,8918340,20066270,6,6,5,5,6,5,4,0,2,2,0,4,1,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0],\
    "Imperial Courier": ["Small","Gutamaya","Small",1,0,6,9,"Std",8,70,2481550,1017200,2288600,4,3,3,1,3,2,3,0,3,0,0,4,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Imperial Cutter": ["Large","Gutamaya","Large",6,12,0,6,"Std",64,720,199926890,83587790,188072510,8,8,7,7,7,7,6,0,4,2,1,8,1,1,1,1,4,3,0,2,0,1,0,0,0,0,0,0],\
    "Imperial Eagle": ["Small","Gutamaya","Small",1,0,8,9,"Std",4,55,72180,66500,2227860,3,3,3,1,2,2,2,2,1,0,0,1,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Imperial Explorer": ["Huge","Gutamaya","None",22,60,0,3,"Exp",128,2200,499793850,250000000,500000000,8,8,8,8,8,8,7,0,2,5,1,8,2,0,0,0,0,2,2,4,0,0,0,0,1,0,0,0],\
    "Keelback": ["Medium","Lakon","Medium",2,0,2,5,"Std",16,350,2943870,1250460,2813540,4,4,4,1,3,2,4,2,2,0,0,3,1,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0],\
    "Krait Lightspeeder": ["Small","Faulcon DeLacy","Small",1,0,6,5,"Std",2,60,21000,31820,103140,2,2,2,1,2,1,1,0,2,0,0,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Krait Mk II": ["Medium","Faulcon DeLacy","Medium",0,0,0,0,"Std",32,0,42409425,22791270,51280360,7,6,5,4,7,6,5,0,2,3,0,4,1,1,2,1,2,2,0,0,0,0,0,0,0,0,0,0],\
    "Krait Phantom": ["Medium","Faulcon DeLacy","Medium",0,0,0,0,"Std",32,0,35589214,22791270,51280360,7,6,5,4,7,6,5,0,2,2,0,4,1,1,3,0,3,1,0,0,0,0,0,0,0,0,0,0],\
    "Mamba": ["Medium","Zorgon Peterson","Medium",0,0,0,0,"Std",8,0,55866341,20626820,46410340,6,5,4,4,6,4,3,2,0,2,1,6,1,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0],\
    "Mamba Mk II": ["Small","Zorgon Peterson","Small",1,0,8,11,"Std",4,60,88750,42880,85400,3,3,2,1,3,2,1,4,0,0,0,1,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Merlin": ["Small","Perez Corporation","Small",2,1,7,9,"Std",8,50,47050,20080,46540,3,3,3,1,2,2,3,2,1,0,0,2,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Mongoose": ["Medium","Zorgon Peterson","Medium",4,0,7,5,"Std",16,270,10024730,4975000,11005140,5,4,4,3,5,4,4,0,6,0,0,0,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0],\
    "Orca": ["Large","Saud Kruger","Large",0,0,0,0,"Std",32,0,47790590,19415950,43685900,5,6,5,6,5,4,5,0,2,1,0,4,1,2,1,1,3,1,0,0,0,0,0,0,0,0,0,0],\
    "Python": ["Medium","Faulcon DeLacy","Medium",4,6,4,5,"Std",32,460,55171380,22791270,51280360,7,6,5,4,7,6,5,0,2,3,0,4,1,1,2,1,2,3,0,0,0,0,0,0,0,0,0,0],\
    "Sidewinder": ["Small","Faulcon DeLacy","Small",1,0,8,6,"Std",2,50,13870,25600,80320,2,2,2,1,1,1,1,2,0,0,0,2,4,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
    "Type-10 Defender": ["Large","Lakon","Large",0,0,0,0,"Std",64,0,121454652,49902137,112279807,8,7,7,5,7,4,6,2,3,4,0,8,1,1,2,2,1,1,1,1,0,0,0,0,2,0,0,0],\
    "Type-6 Transporter": ["Medium","Lakon","Medium",1,2,3,7,"Exp",16,100,865790,418380,941350,3,4,4,2,3,2,4,2,0,0,0,3,1,2,1,2,2,0,0,0,0,0,0,0,0,0,0,0],\
    "Type-7 Transporter": ["Large","Lakon","Large",3,3,2,5,"Std",32,200,16780510,6988900,15725030,5,5,5,4,4,3,5,4,0,0,0,4,1,1,2,0,3,3,0,0,0,0,0,0,0,0,0,0],\
    "Type-9 Heavy": ["Large","Lakon","Large",6,6,0,0,"Std",64,430,72076730,30622340,68900260,6,7,6,5,6,4,6,2,3,0,0,4,1,1,2,2,1,1,1,2,0,0,0,0,0,0,0,0],\
    "Viper Mk III": ["Small","Faulcon DeLacy","Small",1,2,6,9,"Std",4,60,95900,57170,128640,3,3,3,2,3,3,2,2,2,0,0,2,3,1,2,0,0,0,0,0,0,0,1,0,0,0,0,0],\
    "Viper Mk IV": ["Small","Faulcon DeLacy","Small",1,1,5,6,"Std",16,135,310220,175180,394140,4,4,4,2,3,3,4,2,2,0,0,2,3,2,1,2,0,0,0,0,0,0,1,0,0,0,0,0],\
    "Vulture": ["Small","Core Dynamics","Small",1,1,9,7,"Std",8,140,4689640,1970250,4433050,4,5,4,3,5,4,3,0,0,2,0,4,4,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0]
    }

SHIP_WEAPONS = {"SFPL": ["Small Fixed Pulse Laser",1,10,0.39,2,15,15,15,10,10,10,0,"N/A",2200,"N/A","N/A","N/A"],\
    "SGPL": ["Small Gimballed Pulse Laser",1,10,0.39,3,15,15,15,10,10,10,0,"N/A",6600,"N/A","N/A","N/A"],\
    "STPL": ["Small Turreted Pulse Laser",1,10,0.38,2,15,15,15,10,10,10,0,"N/A",26000,"N/A","N/A","N/A"],\
    "SFBL": ["Small Fixed Burst Laser",1,10,0.65,2,10,10,10,5,5,5,10,"N/A",4400,"N/A","N/A","N/A"],\
    "SGBL": ["Small Gimballed Burst Laser",1,10,0.64,3,10,10,10,5,5,5,10,"N/A",8600,"N/A","N/A","N/A"],\
    "STBL": ["Small Turreted Burst Laser",1,10,0.6,2,10,10,10,5,5,5,10,"N/A",52800,"N/A","N/A","N/A"],\
    "SFBL": ["Small Fixed Beam Laser",1,10,0.69,2,10,10,10,5,5,5,20,"N/A",37430,"N/A","N/A","N/A"],\
    "SGBL": ["Small Gimballed Beam Laser",1,10,0.68,3,10,10,10,5,5,5,20,"N/A",74650,"N/A","N/A","N/A"],\
    "STBL": ["Small Turreted Beam Laser",1,10,0.63,2,10,10,10,5,5,5,20,"N/A",500000,"N/A","N/A","N/A"],\
    "SFC": ["Small Fixed Cannon",1,10,0.34,2,10,10,10,15,15,15,0,50,21100,"N/A","N/A","N/A"],\
    "SGC": ["Small Gimballed Cannon",1,10,0.38,3,10,10,10,15,15,15,0,50,42200,"N/A","N/A","N/A"],\
    "STC": ["Small Turreted Cannon",1,10,0.32,2,10,10,10,15,15,15,0,50,506400,"N/A","N/A","N/A"],\
    "SFMC": ["Small Fixed Multi-Cannon",1,10,0.28,2,5,5,5,10,10,10,10,30,9500,"N/A","N/A","N/A"],\
    "SGMC": ["Small Gimballed Multi-Cannon",1,10,0.37,3,5,5,5,10,10,10,10,30,14250,"N/A","N/A","N/A"],\
    "STMC": ["Small Turreted Multi-Cannon",1,10,0.26,2,5,5,5,10,10,10,10,30,81600,"N/A","N/A","N/A"],\
    "SFFC": ["Small Fixed Fragment Cannon",1,10,0.45,4,5,10,15,10,15,20,0,20,36000,"N/A","N/A","CQC Only"],\
    "SGFC": ["Small Gimballed Fragment Cannon",1,10,0.59,5,5,10,15,10,15,20,0,20,54720,"N/A","N/A","CQC Only"],\
    "STFC": ["Small Turreted Fragment Cannon",1,10,0.42,4,5,10,15,10,15,20,0,20,182400,"N/A","N/A","CQC Only"],\
    "SML": ["Small Mine Launcher",1,10,0.4,15,10,10,10,10,10,10,0,6,24260,"N/A","N/A","N/A"],\
    "SFML": ["Small Fixed Mining Laser",1,10,0.5,1,1,1,1,1,1,1,0,"N/A",6800,"Mining",1,],\
    "SSMR": ["Small Seeker Missile Rack",1,10,0.6,4,10,10,10,20,20,20,0,12,72600,"N/A","N/A","N/A"],\
    "SDMR": ["Small Dumbfre Missile Rack",1,10,0.4,1,10,10,10,25,25,25,0,16,32175,"N/A","N/A","N/A"],\
    "STR": ["Small Torpedo Rack",1,10,0.4,-1,15,15,15,35,35,35,0,2,11200,"N/A","N/A","N/A"],\
    "SFR": ["Small Fixed Railgun",1,10,1.15,0,25,25,25,25,25,25,0,10,51600,"N/A","N/A","N/A"],\
    "MFPL": ["Medium Fixed Pulse Laser",2,20,0.6,2,25,25,25,20,20,20,0,"N/A",17600,"N/A","N/A","N/A"],\
    "MGPL": ["Medium Gimballed Pulse Laser",2,20,0.6,3,25,25,25,20,20,20,0,"N/A",35400,"N/A","N/A","N/A"],\
    "MTPL": ["Medium Turreted Pulse Laser",2,20,0.58,2,25,25,25,20,20,20,0,"N/A",132800,"N/A","N/A","N/A"],\
    "MFBL": ["Medium Fixed Burst Laser",2,20,1.05,2,20,20,20,15,15,15,10,"N/A",23000,"N/A","N/A","N/A"],\
    "MGBL": ["Medium Gimballed Burst Laser",2,20,1.04,3,20,20,20,15,15,15,10,"N/A",48500,"N/A","N/A","N/A"],\
    "MTBL": ["Medium Turreted Burst Laser",2,20,0.98,2,20,20,20,15,15,15,10,"N/A",162800,"N/A","N/A","N/A"],\
    "MFBL": ["Medium Fixed Beam Laser",2,20,1.12,2,20,20,20,15,15,15,20,"N/A",299520,"N/A","N/A","N/A"],\
    "MGBL": ["Medium Gimballed Beam Laser",2,20,1.1,3,20,20,20,15,15,15,20,"N/A",500600,"N/A","N/A","N/A"],\
    "MTBL": ["Medium Turreted Beam Laser",2,20,1.03,2,20,20,20,15,15,15,20,"N/A",2099900,"N/A","N/A","N/A"],\
    "MFC": ["Medium Fixed Cannon",2,20,0.49,2,20,20,20,25,25,25,0,50,168430,"N/A","N/A","N/A"],\
    "MGC": ["Medium Gimballed Cannon",2,20,0.54,3,20,20,20,25,25,25,0,50,337600,"N/A","N/A","N/A"],\
    "MTC": ["Medium Turreted Cannon",2,20,0.45,2,20,20,20,25,25,25,0,50,4051200,"N/A","N/A","N/A"],\
    "MFMC": ["Medium Fixed Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,38000,"N/A","N/A","N/A"],\
    "MGMC": ["Medium Gimballed Multi-Cannon",2,20,0.64,3,15,15,15,20,20,20,10,30,57000,"N/A","N/A","N/A"],\
    "MTMC": ["Medium Turreted Multi-Cannon",2,20,0.5,2,15,15,15,20,20,20,10,30,1292800,"N/A","N/A","N/A"],\
    "MFAMC": ["Medium Fixed AX Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,322150,"N/A","N/A","Anti-Thargoid munitions"],\
    "MTAMC": ["Medium Turrented AX Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,1552525,"N/A","N/A","Anti-Thargoid munitions"],\
    "MFFC": ["Medium Fixed Fragment Cannon",2,20,0.74,4,15,20,25,20,25,30,0,20,291840,"N/A","N/A","CQC Only"],\
    "MGFC": ["Medium Gimballed Fragment Cannon",2,20,1.03,5,15,20,25,20,25,30,0,20,437760,"N/A","N/A","CQC Only"],\
    "MTFC": ["Medium Turreted Fragment Cannon",2,20,0.79,4,15,20,25,20,25,30,0,20,1459200,"N/A","N/A","CQC Only"],\
    "MFPA": ["Medium Fixed Plasma Accelerator",2,20,1.43,-1,50,50,50,50,50,50,0,50,834200,"N/A","N/A","N/A"],\
    "MML": ["Medium Mine Launcher",2,20,0.4,17,20,20,20,20,20,20,0,6,294080,"N/A","N/A","N/A"],\
    "MFML": ["Medium Fixed Mining Laser",2,20,0.75,1,1,1,1,1,1,1,0,"N/A",22580,"Mining",1,"N/A"],\
    "MSMR": ["Medium Seeker Missile Rack",2,20,1.2,4,15,15,15,35,35,35,0,12,512400,"N/A","N/A","N/A"],\
    "MDMR": ["Medium Dumbfre Missile Rack",2,20,1.2,1,20,20,20,40,40,40,0,16,240400,"N/A","N/A","N/A"],\
    "MTP": ["Medium Torpedo Pylon",2,20,0.4,-1,25,25,25,50,50,50,0,2,44800,"N/A","N/A","N/A"],\
    "MAMR": ["Medium AX Missle Rack",2,20,1.2,1,20,20,20,40,40,40,0,32,40900,"N/A","N/A","Anti-Thargoid munitions"],\
    "MFR": ["Medium Fixed Railgun",2,20,1.63,0,40,40,40,40,40,40,0,10,412800,"N/A","N/A","N/A"],\
    "MFFL": ["Medium Fixed Flak Launcher",2,20,1.2,4,20,20,20,20,20,20,0,30,261800,"N/A","N/A","Inflicts full damage on Thargon Swarms"],\
    "MTFL": ["Medium Turreted Flak Launcher",2,20,1.2,4,20,20,20,20,20,20,0,30,1259200,"N/A","N/A","Inflicts full damage on Thargon Swarms"],\
    "LFPL": ["Large Fixed Pulse Laser",3,30,0.9,2,35,35,35,30,30,30,0,"N/A",70400,"N/A","N/A","N/A"],\
    "LGPL": ["Large Gimballed Pulse Laser",3,30,0.92,3,35,35,35,30,30,30,0,"N/A",140600,"N/A","N/A","N/A"],\
    "LTPL": ["Large Turreted Pulse Laser",3,30,0.89,2,35,35,35,30,30,30,0,"N/A",400400,"N/A","N/A","N/A"],\
    "LFBL": ["Large Fixed Burst Laser",3,30,1.66,2,30,30,30,25,25,25,10,"N/A",140400,"N/A","N/A","N/A"],\
    "LGBL": ["Large Gimballed Burst Laser",3,30,1.65,3,30,30,30,25,25,25,10,"N/A",281600,"N/A","N/A","N/A"],\
    "LTBL": ["Large Turreted Burst Laser",3,30,1.57,2,30,30,30,25,25,25,10,"N/A",800400,"N/A","N/A","N/A"],\
    "LFBL": ["Large Fixed Beam Laser",3,30,1.8,2,30,30,30,25,25,25,20,"N/A",1177600,"N/A","N/A","N/A"],\
    "LGBL": ["Large Gimballed Beam Laser",3,30,1.78,3,30,30,30,25,25,25,20,"N/A",2396160,"N/A","N/A","N/A"],\
    "LTBL": ["Large Turreted Beam Laser",3,30,1.68,2,30,30,30,25,25,25,20,"N/A",19399600,"N/A","N/A","N/A"],\
    "LFC": ["Large Fixed Cannon",3,30,0.67,2,30,30,30,35,35,35,0,50,675200,"N/A","N/A","N/A"],\
    "LGC": ["Large Gimballed Cannon",3,30,0.75,3,30,30,30,35,35,35,0,50,1350400,"N/A","N/A","N/A"],\
    "LTCL": ["Large Turreted Cannon",3,30,0.64,2,30,30,30,35,35,35,0,50,16204800,"N/A","N/A","N/A"],\
    "LFFC": ["Large Fixed Fragment Cannon",3,30,1.02,4,25,30,35,30,35,40,0,20,1167360,"N/A","N/A","CQC Only"],\
    "LGFC": ["Large Gimballed Fragment Cannon",3,30,1.55,5,25,30,35,30,35,40,0,20,1751040,"N/A","N/A","CQC Only"],\
    "LTFC": ["Large Turreted Fragment Cannon",3,30,1.29,4,25,30,35,30,35,40,0,20,5836800,"N/A","N/A","CQC Only"],\
    "LFMC": ["Large Fixed Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,140400,"N/A","N/A","N/A"],\
    "LFAMC": ["Large Fixed AX Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,1151963,"N/A","N/A","Anti-Thargoid munitions"],\
    "LGMC": ["Large Gimballed Multi-Cannon",3,30,0.97,3,25,25,25,30,30,30,10,30,578450,"N/A","N/A","N/A"],\
    "LTAMC": ["Large Turreted AX Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,3726060,"N/A","N/A","Anti-Thargoid munitions"],\
    "LFPA": ["Large Fixed Plasma Accelerator",3,30,1.97,-1,60,60,60,60,60,60,0,50,3051200,"N/A","N/A","N/A"],\
    "LAMR": ["Large AX Missile Rack",3,30,1.62,1,30,30,30,60,60,60,0,64,1318444,"N/A","N/A","Anti-Thargoid munitions"],\
    "HFPL": ["Huge Fixed Pulse Laser",4,40,1.33,2,45,45,45,40,40,40,0,"N/A",177600,"N/A","N/A","N/A"],\
    "HGPL": ["Huge Gimballed Pulse Laser",4,40,1.37,3,45,45,45,40,40,40,0,"N/A",877600,"N/A","N/A","N/A"],\
    "HFBL": ["Huge Fixed Burst Laser",4,40,2.58,2,40,40,40,35,35,35,10,"N/A",281600,"N/A","N/A","N/A"],\
    "HGBL": ["Huge Gimballed Burst Laser",4,40,2.59,3,40,40,40,35,35,35,10,"N/A",1245600,"N/A","N/A","N/A"],\
    "HFBL": ["Huge Fixed Beam Laser",4,40,2.9,2,40,40,40,35,35,35,20,"N/A",2396160,"N/A","N/A","N/A"],\
    "HGBL": ["Huge Gimballed Beam Laser",4,40,2.86,3,40,40,40,35,35,35,20,"N/A",8746160,"N/A","N/A","N/A"],\
    "HFC": ["Huge Fixed Cannon",4,40,0.92,2,40,40,40,45,45,45,0,50,2700800,"N/A","N/A","N/A"],\
    "HGC": ["Huge Gimballed Cannon",4,40,1.03,3,40,40,40,45,45,45,0,50,5401600,"N/A","N/A","N/A"],\
    "HFMC": ["Huge Fixed Multi-Cannon",4,40,0.73,2,35,35,35,40,40,40,10,30,1177600,"N/A","N/A","N/A"],\
    "HGMC": ["Huge Gimballed Multi-Cannon",4,40,1.22,3,35,35,35,40,40,40,10,30,6377600,"N/A","N/A","N/A"],\
    "HFPL": ["Huge Fixed Plasma Accelerator",4,40,2.63,-1,70,70,70,70,70,70,0,50,13793600,"N/A","N/A","N/A"]
    }

UTILITIES = {"Chaff": ["Chaff Launcher","U",10,0.2,"N/A","You can activate your Chaff Launcher as an Equipment Action. +4 defence against gimballed and automated turret attacks until your next turn starts.",6,8500,"N/A",0],\
    "ECM": ["EMC","U",10,0.2,"N/A","You gain a continual +4 defence bonus against Seeker Missile attacks.","N/A",12500,"N/A",0],\
    "Heat sink": ["Heat Sink Launcher","U",10,0.2,"N/A","When activated you gain a +2 System bonus when Silent Running.",4,3500,"N/A",0],\
    "Point def": ["Point Defence","U",10,0.2,"N/A","Automatically activates when a missile, torpedo or mine would hit you. Roll a D10. On an even score the missile or mine is destroyed.",10,18546,"N/A",0],\
    "Manifest E": ["Manifest Scanner E grade","U",10,0.2,"E","Allows you to scan nearby ships to determine their cargo.","N/A",13544,"N/A",0],\
    "Manifest D": ["Manifest Scanner D grade","U",10,0.4,"D","Allows you to scan nearby ships with a +1 bonus to your Systems Skill Check to determine their cargo.","N/A",40633,"N/A",0],\
    "Manifest C": ["Manifest Scanner C grade","U",10,0.8,"C","Allows you to scan nearby ships with a +2 bonus to your Systems Skill Check to determine their cargo.","N/A",121899,"N/A",0],\
    "Manifest B": ["Manifest Scanner B grade","U",10,1.6,"B","Allows you to scan nearby ships with a +3 bonus to your Systems Skill Check to determine their cargo.","N/A",365698,"N/A",0],\
    "Manifest A": ["Manifest Scanner A grade","U",10,3.2,"A","Allows you to scan nearby ships with a +4 bonus to your Systems Skill Check to determine their cargo.","N/A",1097095,"N/A",0],\
    "Wake E": ["Frame Shift Wake Scanner E grade","U",10,0.2,"E","Allows you to determine the hyperspace destination of a ship that has just jumped.","N/A",13544,"N/A",0],\
    "Wake D": ["Frame Shift Wake Scanner D grade","U",10,0.4,"D","Allows you to determine the hyperspace destination of a ship that has just jumped. You gain a +1 bonus to your Systems check when you do so.","N/A",40633,"N/A",0],\
    "Wake C": ["Frame Shift Wake Scanner C grade","U",10,0.8,"C","Allows you to determine the hyperspace destination of a ship that has just jumped. You gain a +2 bonus to your Systems check when you do so.","N/A",121899,"N/A",0],\
    "Wake B": ["Frame Shift Wake Scanner B grade","U",10,1.6,"B","Allows you to determine the hyperspace destination of a ship that has just jumped. You gain a +3 bonus to your Systems check when you do so.","N/A",365698,"N/A",0],\
    "Wake A": ["Frame Shift Wake Scanner A grade","U",10,3.2,"A","Allows you to determine the hyperspace destination of a ship that has just jumped. You gain a +4 bonus to your Systems check when you do so.","N/A",1097095,"N/A",0],\
    "Warrent E": ["Kill Warrant Scanner E grade","U",10,0.2,"E","This scanner and communications computer gives you a 20% bounty reward bonus","N/A",13544,"N/A",0],\
    "Warrent D": ["Kill Warrant Scanner D grade","U",10,0.4,"D","This scanner and communications computer gives you a 40% bounty reward bonus","N/A",40633,"N/A",0],\
    "Warrent C": ["Kill Warrant Scanner C grade","U",10,0.8,"C","This scanner and communications computer gives you a 60% bounty reward bonus","N/A",121899,"N/A",0],\
    "Warrent B": ["Kill Warrant Scanner B grade","U",10,1.6,"B","This scanner and communications computer gives you a 80% bounty reward bonus","N/A",365698,"N/A",0],\
    "Warrent A": ["Kill Warrant Scanner A grade","U",10,3.2,"A","This scanner and communications computer gives you a 100% bounty reward bonus","N/A",1097095,"N/A",0],\
    "Sld Boost E": ["Shield Booster E grade","U",10,0.2,"E","Gain a 5% boost to your Shield score.","N/A",10000,["Shields",1.05]],\
    "Sld Boost D": ["Shield Booster D grade","U",10,0.5,"D","Gain a 10% boost to your Shield score.","N/A",23000,["Shields",1.1]],\
    "Sld Boost C": ["Shield Booster C grade","U",10,0.7,"C","Gain a 15% boost to your Shield score.","N/A",53000,["Shields",1.15]],\
    "Sld Boost B": ["Shield Booster B grade","U",10,1.0,"B","Gain a 20% boost to your Shield score.","N/A",122000,["Shields",1.2]],\
    "Sld Boost A": ["Shield Booster A grade","U",10,1.2,"A","Gain a 25% boost to your Shield score.","N/A",281000,["Shields",1.25]]\
    }

POWERPLANT = {"PP 2E": ("Power Plant 2E","2","E",6.4,20,1980),\
    "PP 2D": ("Power Plant 2D","2","D",7.2,20,5930),\
    "PP 2C": ("Power Plant 2C","2","C",8.0,25,17800),\
    "PP 2B": ("Power Plant 2B","2","B",8.8,25,53410),\
    "PP 2A": ("Power Plant 2A","2","A",9.6,30,160220),\
    "PP 3E": ("Power Plant 3E","3","E",8.0,30,6200),\
    "PP 3D": ("Power Plant 3D","3","D",9.0,30,18810),\
    "PP 3C": ("Power Plant 3C","3","C",10.0,35,56440),\
    "PP 3B": ("Power Plant 3B","3","B",11.0,35,169300),\
    "PP 3A": ("Power Plant 3A","3","A",12.0,40,507910),\
    "PP 4E": ("Power Plant 4E","4","E",10.4,40,19880),\
    "PP 4D": ("Power Plant 4D","4","D",11.7,40,59630),\
    "PP 4C": ("Power Plant 4C","4","C",13.0,45,178900),\
    "PP 4B": ("Power Plant 4B","4","B",14.3,45,536690),\
    "PP 4A": ("Power Plant 4A","4","A",15.6,50,1610080),\
    "PP 5E": ("Power Plant 5E","5","E",13.6,50,63010),\
    "PP 5D": ("Power Plant 5D","5","D",15.3,50,189040),\
    "PP 5C": ("Power Plant 5C","5","C",17.0,55,567110),\
    "PP 5B": ("Power Plant 5B","5","B",18.7,55,1701320),\
    "PP 5A": ("Power Plant 5A","5","A",20.4,60,5103950),\
    "PP 6E": ("Power Plant 6E","6","E",16.8,60,199750),\
    "PP 6D": ("Power Plant 6D","6","D",18.9,60,599240),\
    "PP 6C": ("Power Plant 6C","6","C",21.0,65,1797730),\
    "PP 6B": ("Power Plant 6B","6","B",23.1,65,5393180),\
    "PP 6A": ("Power Plant 6A","6","A",25.2,70,16179530),\
    "PP 7E": ("Power Plant 7E","7","E",20.0,70,633200),\
    "PP 7D": ("Power Plant 7D","7","D",22.5,70,1899600),\
    "PP 7C": ("Power Plant 7C","7","C",25.0,75,5698790),\
    "PP 7B": ("Power Plant 7B","7","B",27.5,75,17096370),\
    "PP 7A": ("Power Plant 7A","7","A",30.0,80,51289110),\
    "PP 8E": ("Power Plant 8E","8","E",24.0,80,2007240),\
    "PP 8D": ("Power Plant 8D","8","D",27.0,80,6021720),\
    "PP 8C": ("Power Plant 8C","8","C",30.0,85,18065170),\
    "PP 8B": ("Power Plant 8B","8","B",33.0,85,54195500),\
    "PP 8A": ("Power Plant 8A","8","A",36.0,90,162586490)
    }
