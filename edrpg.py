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
        self.text = "Empty"



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