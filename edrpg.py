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
        self.backgrounds_max = 5
        self.backgrounds = []
        self.enhancements_max = 0
        self.enhancements = []
        self.karam_capab_max = 4
        self.karam_capab = []
        self.carried_weap_max = 2
        self.carried_weap = []
        self.clip_grenade_max = 2
        self.clip_grenade = []
        self.clothing = []
        self.pack_inv = []
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
        self.sleight = Skill("Sleight of Hand", "E")
        self.stealth = Skill("Stealth", "E")
        self.surv = Skill("Survival", "E")


class Skill:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
        self.cap = 40
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


class Background:
    def __init__(self,code):
        self.name = BACKGROUNDS[code][0]
        self.cost = BACKGROUNDS[code][1]
        self.effects = BACKGROUNDS[code][2]
        self.enhance = BACKGROUNDS[code][3]
        self.spec = BACKGROUNDS[code][4]
        self.descript = BACKGROUNDS[code][5]

class Karma_capab:
    def __init__(self,code):
        self.name = KARMA_CAPABS[code][0]
        self.cost = KARMA_CAPABS[code][1]
        self.ship_comb = KARMA_CAPABS[code][2]
        self.veh_comb = KARMA_CAPABS[code][3]
        self.pers_comb = KARMA_CAPABS[code][4]
        self.effect = KARMA_CAPABS[code][5]
        self.prereq = KARMA_CAPABS[code][6]
        self.special = KARMA_CAPABS[code][7]
        self.descript = KARMA_CAPABS[code][8]


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
                self.u += 100
        elif self.u >= 100:
            self.mcr += self.u // 100 
            self.u = self.u % 100

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
        self.manufacturer = SHIPS[self.model][1]
        self.landing_pad = SHIPS[self.model][2]
        
        # general
        self.crew = SHIPS[self.model][3]
        self.passengers = SHIPS[self.model][4]
        self.agility = SHIPS[self.model][5]
        self.speed = SHIPS[self.model][6]
        self.range = SHIPS[self.model][7]
        self.fuel = 0
        self.hull = SHIPS[self.model][9]
        self.shields = 0
        self.shield_recharge = 5
        self.float_pts = 0

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
        self.pd_slot = Slot(SHIPS[self.model][14])
        self.ss_slot = Slot(SHIPS[self.model][15])
        self.ft_slot = Slot(SHIPS[self.model][16])
        self.weapon_slots = []
        self.utility_mounts = []
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
        self.name = SHIP_WEAPONS[code][0]
        self.size = SHIP_WEAPONS[code][1]
        self.strength = SHIP_WEAPONS[code][2]
        self.pwr = SHIP_WEAPONS[code][3]
        self.to_hit = SHIP_WEAPONS[code][4]
        self.sld_sml = SHIP_WEAPONS[code][5]
        self.sld_med = SHIP_WEAPONS[code][6]
        self.sld_lrg = SHIP_WEAPONS[code][7]
        self.amr_sml = SHIP_WEAPONS[code][8]
        self.arm_med = SHIP_WEAPONS[code][9]
        self.arm_lrg = SHIP_WEAPONS[code][10]
        self.burst = SHIP_WEAPONS[code][11]
        self.ammo = SHIP_WEAPONS[code][12]
        self.cost = SHIP_WEAPONS[code][13]
        self.effect = SHIP_WEAPONS[code][14]
        self.effect_amt = SHIP_WEAPONS[code][15]
        self.notes(SHIP_WEAPONS[code][16])


class Utility:
    def __init__(self, code):
        self.name = UTILITIES[code][0]
        self.size = UTILITIES[code][1]
        self.strength = UTILITIES[code][2]
        self.pwr = UTILITIES[code][3]
        self.model = UTILITIES[code][4]
        self.desr = UTILITIES[code][5]
        self.ammo = UTILITIES[code][6]
        self.cost = UTILITIES[code][7]
        self.effect = UTILITIES[code][8]
        self.effect_amt = UTILITIES[code][9]


class Power_plant:
    def __init__(self,code):
        self.name = POWERPLANT[code][0]
        self.size = POWERPLANT[code][1]
        self.model = POWERPLANT[code][2]
        self.power = POWERPLANT[code][3]
        self.strength = POWERPLANT[code][4]
        self.cost = POWERPLANT[code][5]


class Thusters:
    def __init__(self,code):
        self.name = THUSTERS[code][0]
        self.size = THUSTERS[code][1]
        self.model = THUSTERS[code][2]
        self.power = THUSTERS[code][3]
        self.strength = THUSTERS[code][4]
        self.effects = THUSTERS[code][5]
        self.cost = THUSTERS[code][6]


class Fsd:
    def __init__(self,code):
        self.name = FSD[code][0]
        self.size = FSD[code][1]
        self.model = FSD[code][2]
        self.power = FSD[code][3]
        self.strength = FSD[code][4]
        self.range = FSD[code][5]
        self.cost = FSD[code][6]


class Life_Support:
    def __init__(self,code):
        self.name = LIFE_SUPPORT[code][0]
        self.size = LIFE_SUPPORT[code][1]
        self.model = LIFE_SUPPORT[code][2]
        self.power = LIFE_SUPPORT[code][3]
        self.strength = LIFE_SUPPORT[code][4]
        self.duration = LIFE_SUPPORT[code][5]
        self.cost = LIFE_SUPPORT[code][6]


class Power_Dist:
    def __init__(self,code):
        self.name = POWER_DIST[code][0]
        self.size = POWER_DIST[code][1]
        self.model = POWER_DIST[code][2]
        self.power = POWER_DIST[code][3]
        self.strength = POWER_DIST[code][4]
        self.effects = POWER_DIST[code][5]
        self.cost = POWER_DIST[code][6]


class Sensors:
    def __init__(self,code):
        self.name = SENSORS[code][0]
        self.size = SENSORS[code][1]
        self.model = SENSORS[code][2]
        self.power = SENSORS[code][3]
        self.strength = SENSORS[code][4]
        self.effects = SENSORS[code][5]
        self.cost = SENSORS[code][6]


class Fuel_tank:
    def __init__(self,code):
        self.name = FUEL_TANK[code][0]
        self.size = FUEL_TANK[code][1]
        self.tonnage = FUEL_TANK[2]
        self.cost = FUEL_TANK[3]

class Effect:
    def __init__(self,stat, amt):
        self.stat = stat
        self.amt = amt


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

SHIP_WEAPONS = {"SFPL": ["Small Fixed Pulse Laser",1,10,0.39,2,15,15,15,10,10,10,0,"N/A",2200,"N/A","N/A"],\
    "SGPL": ["Small Gimballed Pulse Laser",1,10,0.39,3,15,15,15,10,10,10,0,"N/A",6600,"N/A","N/A"],\
    "STPL": ["Small Turreted Pulse Laser",1,10,0.38,2,15,15,15,10,10,10,0,"N/A",26000,"N/A","N/A"],\
    "SFBL": ["Small Fixed Burst Laser",1,10,0.65,2,10,10,10,5,5,5,10,"N/A",4400,"N/A","N/A"],\
    "SGBL": ["Small Gimballed Burst Laser",1,10,0.64,3,10,10,10,5,5,5,10,"N/A",8600,"N/A","N/A"],\
    "STBL": ["Small Turreted Burst Laser",1,10,0.6,2,10,10,10,5,5,5,10,"N/A",52800,"N/A","N/A"],\
    "SFBL": ["Small Fixed Beam Laser",1,10,0.69,2,10,10,10,5,5,5,20,"N/A",37430,"N/A","N/A"],\
    "SGBL": ["Small Gimballed Beam Laser",1,10,0.68,3,10,10,10,5,5,5,20,"N/A",74650,"N/A","N/A"],\
    "STBL": ["Small Turreted Beam Laser",1,10,0.63,2,10,10,10,5,5,5,20,"N/A",500000,"N/A","N/A"],\
    "SFC": ["Small Fixed Cannon",1,10,0.34,2,10,10,10,15,15,15,0,50,21100,"N/A","N/A"],\
    "SGC": ["Small Gimballed Cannon",1,10,0.38,3,10,10,10,15,15,15,0,50,42200,"N/A","N/A"],\
    "STC": ["Small Turreted Cannon",1,10,0.32,2,10,10,10,15,15,15,0,50,506400,"N/A","N/A"],\
    "SFMC": ["Small Fixed Multi-Cannon",1,10,0.28,2,5,5,5,10,10,10,10,30,9500,"N/A","N/A"],\
    "SGMC": ["Small Gimballed Multi-Cannon",1,10,0.37,3,5,5,5,10,10,10,10,30,14250,"N/A","N/A"],\
    "STMC": ["Small Turreted Multi-Cannon",1,10,0.26,2,5,5,5,10,10,10,10,30,81600,"N/A","N/A"],\
    "SFFC": ["Small Fixed Fragment Cannon",1,10,0.45,4,5,10,15,10,15,20,0,20,36000,"N/A","CQC Only"],\
    "SGFC": ["Small Gimballed Fragment Cannon",1,10,0.59,5,5,10,15,10,15,20,0,20,54720,"N/A","CQC Only"],\
    "STFC": ["Small Turreted Fragment Cannon",1,10,0.42,4,5,10,15,10,15,20,0,20,182400,"N/A","CQC Only"],\
    "SML": ["Small Mine Launcher",1,10,0.4,15,10,10,10,10,10,10,0,6,24260,"N/A","N/A"],\
    "SFML": ["Small Fixed Mining Laser",1,10,0.5,1,1,1,1,1,1,1,0,"N/A",6800,Effect("Mining",1),"N/A"],\
    "SSMR": ["Small Seeker Missile Rack",1,10,0.6,4,10,10,10,20,20,20,0,12,72600,"N/A","N/A"],\
    "SDMR": ["Small Dumbfre Missile Rack",1,10,0.4,1,10,10,10,25,25,25,0,16,32175,"N/A","N/A"],\
    "STR": ["Small Torpedo Rack",1,10,0.4,-1,15,15,15,35,35,35,0,2,11200,"N/A","N/A"],\
    "SFR": ["Small Fixed Railgun",1,10,1.15,0,25,25,25,25,25,25,0,10,51600,"N/A","N/A"],\
    "MFPL": ["Medium Fixed Pulse Laser",2,20,0.6,2,25,25,25,20,20,20,0,"N/A",17600,"N/A","N/A"],\
    "MGPL": ["Medium Gimballed Pulse Laser",2,20,0.6,3,25,25,25,20,20,20,0,"N/A",35400,"N/A","N/A"],\
    "MTPL": ["Medium Turreted Pulse Laser",2,20,0.58,2,25,25,25,20,20,20,0,"N/A",132800,"N/A","N/A"],\
    "MFBL": ["Medium Fixed Burst Laser",2,20,1.05,2,20,20,20,15,15,15,10,"N/A",23000,"N/A","N/A"],\
    "MGBL": ["Medium Gimballed Burst Laser",2,20,1.04,3,20,20,20,15,15,15,10,"N/A",48500,"N/A","N/A"],\
    "MTBL": ["Medium Turreted Burst Laser",2,20,0.98,2,20,20,20,15,15,15,10,"N/A",162800,"N/A","N/A"],\
    "MFBL": ["Medium Fixed Beam Laser",2,20,1.12,2,20,20,20,15,15,15,20,"N/A",299520,"N/A","N/A"],\
    "MGBL": ["Medium Gimballed Beam Laser",2,20,1.1,3,20,20,20,15,15,15,20,"N/A",500600,"N/A","N/A"],\
    "MTBL": ["Medium Turreted Beam Laser",2,20,1.03,2,20,20,20,15,15,15,20,"N/A",2099900,"N/A","N/A"],\
    "MFC": ["Medium Fixed Cannon",2,20,0.49,2,20,20,20,25,25,25,0,50,168430,"N/A","N/A"],\
    "MGC": ["Medium Gimballed Cannon",2,20,0.54,3,20,20,20,25,25,25,0,50,337600,"N/A","N/A"],\
    "MTC": ["Medium Turreted Cannon",2,20,0.45,2,20,20,20,25,25,25,0,50,4051200,"N/A","N/A"],\
    "MFMC": ["Medium Fixed Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,38000,"N/A","N/A"],\
    "MGMC": ["Medium Gimballed Multi-Cannon",2,20,0.64,3,15,15,15,20,20,20,10,30,57000,"N/A","N/A"],\
    "MTMC": ["Medium Turreted Multi-Cannon",2,20,0.5,2,15,15,15,20,20,20,10,30,1292800,"N/A","N/A"],\
    "MFAMC": ["Medium Fixed AX Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,322150,"N/A","Anti-Thargoid munitions"],\
    "MTAMC": ["Medium Turrented AX Multi-Cannon",2,20,0.46,2,15,15,15,20,20,20,10,30,1552525,"N/A","Anti-Thargoid munitions"],\
    "MFFC": ["Medium Fixed Fragment Cannon",2,20,0.74,4,15,20,25,20,25,30,0,20,291840,"N/A","CQC Only"],\
    "MGFC": ["Medium Gimballed Fragment Cannon",2,20,1.03,5,15,20,25,20,25,30,0,20,437760,"N/A","CQC Only"],\
    "MTFC": ["Medium Turreted Fragment Cannon",2,20,0.79,4,15,20,25,20,25,30,0,20,1459200,"N/A","CQC Only"],\
    "MFPA": ["Medium Fixed Plasma Accelerator",2,20,1.43,-1,50,50,50,50,50,50,0,50,834200,"N/A","N/A"],\
    "MML": ["Medium Mine Launcher",2,20,0.4,17,20,20,20,20,20,20,0,6,294080,"N/A","N/A"],\
    "MFML": ["Medium Fixed Mining Laser",2,20,0.75,1,1,1,1,1,1,1,0,"N/A",22580,Effect("Mining",1),"N/A"],\
    "MSMR": ["Medium Seeker Missile Rack",2,20,1.2,4,15,15,15,35,35,35,0,12,512400,"N/A","N/A"],\
    "MDMR": ["Medium Dumbfre Missile Rack",2,20,1.2,1,20,20,20,40,40,40,0,16,240400,"N/A","N/A"],\
    "MTP": ["Medium Torpedo Pylon",2,20,0.4,-1,25,25,25,50,50,50,0,2,44800,"N/A","N/A"],\
    "MAMR": ["Medium AX Missle Rack",2,20,1.2,1,20,20,20,40,40,40,0,32,40900,"N/A","Anti-Thargoid munitions"],\
    "MFR": ["Medium Fixed Railgun",2,20,1.63,0,40,40,40,40,40,40,0,10,412800,"N/A","N/A"],\
    "MFFL": ["Medium Fixed Flak Launcher",2,20,1.2,4,20,20,20,20,20,20,0,30,261800,"N/A","Inflicts full damage on Thargon Swarms"],\
    "MTFL": ["Medium Turreted Flak Launcher",2,20,1.2,4,20,20,20,20,20,20,0,30,1259200,"N/A","Inflicts full damage on Thargon Swarms"],\
    "LFPL": ["Large Fixed Pulse Laser",3,30,0.9,2,35,35,35,30,30,30,0,"N/A",70400,"N/A","N/A"],\
    "LGPL": ["Large Gimballed Pulse Laser",3,30,0.92,3,35,35,35,30,30,30,0,"N/A",140600,"N/A","N/A"],\
    "LTPL": ["Large Turreted Pulse Laser",3,30,0.89,2,35,35,35,30,30,30,0,"N/A",400400,"N/A","N/A"],\
    "LFBL": ["Large Fixed Burst Laser",3,30,1.66,2,30,30,30,25,25,25,10,"N/A",140400,"N/A","N/A"],\
    "LGBL": ["Large Gimballed Burst Laser",3,30,1.65,3,30,30,30,25,25,25,10,"N/A",281600,"N/A","N/A"],\
    "LTBL": ["Large Turreted Burst Laser",3,30,1.57,2,30,30,30,25,25,25,10,"N/A",800400,"N/A","N/A"],\
    "LFBL": ["Large Fixed Beam Laser",3,30,1.8,2,30,30,30,25,25,25,20,"N/A",1177600,"N/A","N/A"],\
    "LGBL": ["Large Gimballed Beam Laser",3,30,1.78,3,30,30,30,25,25,25,20,"N/A",2396160,"N/A","N/A"],\
    "LTBL": ["Large Turreted Beam Laser",3,30,1.68,2,30,30,30,25,25,25,20,"N/A",19399600,"N/A","N/A"],\
    "LFC": ["Large Fixed Cannon",3,30,0.67,2,30,30,30,35,35,35,0,50,675200,"N/A","N/A"],\
    "LGC": ["Large Gimballed Cannon",3,30,0.75,3,30,30,30,35,35,35,0,50,1350400,"N/A","N/A"],\
    "LTCL": ["Large Turreted Cannon",3,30,0.64,2,30,30,30,35,35,35,0,50,16204800,"N/A","N/A"],\
    "LFFC": ["Large Fixed Fragment Cannon",3,30,1.02,4,25,30,35,30,35,40,0,20,1167360,"N/A","CQC Only"],\
    "LGFC": ["Large Gimballed Fragment Cannon",3,30,1.55,5,25,30,35,30,35,40,0,20,1751040,"N/A","CQC Only"],\
    "LTFC": ["Large Turreted Fragment Cannon",3,30,1.29,4,25,30,35,30,35,40,0,20,5836800,"N/A","CQC Only"],\
    "LFMC": ["Large Fixed Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,140400,"N/A","N/A"],\
    "LFAMC": ["Large Fixed AX Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,1151963,"N/A","Anti-Thargoid munitions"],\
    "LGMC": ["Large Gimballed Multi-Cannon",3,30,0.97,3,25,25,25,30,30,30,10,30,578450,"N/A","N/A"],\
    "LTAMC": ["Large Turreted AX Multi-Cannon",3,30,0.64,2,25,25,25,30,30,30,10,30,3726060,"N/A","Anti-Thargoid munitions"],\
    "LFPA": ["Large Fixed Plasma Accelerator",3,30,1.97,-1,60,60,60,60,60,60,0,50,3051200,"N/A","N/A"],\
    "LAMR": ["Large AX Missile Rack",3,30,1.62,1,30,30,30,60,60,60,0,64,1318444,"N/A","Anti-Thargoid munitions"],\
    "HFPL": ["Huge Fixed Pulse Laser",4,40,1.33,2,45,45,45,40,40,40,0,"N/A",177600,"N/A","N/A"],\
    "HGPL": ["Huge Gimballed Pulse Laser",4,40,1.37,3,45,45,45,40,40,40,0,"N/A",877600,"N/A","N/A"],\
    "HFBL": ["Huge Fixed Burst Laser",4,40,2.58,2,40,40,40,35,35,35,10,"N/A",281600,"N/A","N/A"],\
    "HGBL": ["Huge Gimballed Burst Laser",4,40,2.59,3,40,40,40,35,35,35,10,"N/A",1245600,"N/A","N/A"],\
    "HFBL": ["Huge Fixed Beam Laser",4,40,2.9,2,40,40,40,35,35,35,20,"N/A",2396160,"N/A","N/A"],\
    "HGBL": ["Huge Gimballed Beam Laser",4,40,2.86,3,40,40,40,35,35,35,20,"N/A",8746160,"N/A","N/A"],\
    "HFC": ["Huge Fixed Cannon",4,40,0.92,2,40,40,40,45,45,45,0,50,2700800,"N/A","N/A"],\
    "HGC": ["Huge Gimballed Cannon",4,40,1.03,3,40,40,40,45,45,45,0,50,5401600,"N/A","N/A"],\
    "HFMC": ["Huge Fixed Multi-Cannon",4,40,0.73,2,35,35,35,40,40,40,10,30,1177600,"N/A","N/A"],\
    "HGMC": ["Huge Gimballed Multi-Cannon",4,40,1.22,3,35,35,35,40,40,40,10,30,6377600,"N/A","N/A"],\
    "HFPL": ["Huge Fixed Plasma Accelerator",4,40,2.63,-1,70,70,70,70,70,70,0,50,13793600,"N/A","N/A"]
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

POWERPLANT = {"PP 2E": ("Power Plant 2E",2,"E",6.4,20,1980),\
    "PP 2D": ("Power Plant 2D",2,"D",7.2,20,5930),\
    "PP 2C": ("Power Plant 2C",2,"C",8.0,25,17800),\
    "PP 2B": ("Power Plant 2B",2,"B",8.8,25,53410),\
    "PP 2A": ("Power Plant 2A",2,"A",9.6,30,160220),\
    "PP 3E": ("Power Plant 3E",3,"E",8.0,30,6200),\
    "PP 3D": ("Power Plant 3D",3,"D",9.0,30,18810),\
    "PP 3C": ("Power Plant 3C",3,"C",10.0,35,56440),\
    "PP 3B": ("Power Plant 3B",3,"B",11.0,35,169300),\
    "PP 3A": ("Power Plant 3A",3,"A",12.0,40,507910),\
    "PP 4E": ("Power Plant 4E",4,"E",10.4,40,19880),\
    "PP 4D": ("Power Plant 4D",4,"D",11.7,40,59630),\
    "PP 4C": ("Power Plant 4C",4,"C",13.0,45,178900),\
    "PP 4B": ("Power Plant 4B",4,"B",14.3,45,536690),\
    "PP 4A": ("Power Plant 4A",4,"A",15.6,50,1610080),\
    "PP 5E": ("Power Plant 5E",5,"E",13.6,50,63010),\
    "PP 5D": ("Power Plant 5D",5,"D",15.3,50,189040),\
    "PP 5C": ("Power Plant 5C",5,"C",17.0,55,567110),\
    "PP 5B": ("Power Plant 5B",5,"B",18.7,55,1701320),\
    "PP 5A": ("Power Plant 5A",5,"A",20.4,60,5103950),\
    "PP 6E": ("Power Plant 6E",6,"E",16.8,60,199750),\
    "PP 6D": ("Power Plant 6D",6,"D",18.9,60,599240),\
    "PP 6C": ("Power Plant 6C",6,"C",21.0,65,1797730),\
    "PP 6B": ("Power Plant 6B",6,"B",23.1,65,5393180),\
    "PP 6A": ("Power Plant 6A",6,"A",25.2,70,16179530),\
    "PP 7E": ("Power Plant 7E",7,"E",20.0,70,633200),\
    "PP 7D": ("Power Plant 7D",7,"D",22.5,70,1899600),\
    "PP 7C": ("Power Plant 7C",7,"C",25.0,75,5698790),\
    "PP 7B": ("Power Plant 7B",7,"B",27.5,75,17096370),\
    "PP 7A": ("Power Plant 7A",7,"A",30.0,80,51289110),\
    "PP 8E": ("Power Plant 8E",8,"E",24.0,80,2007240),\
    "PP 8D": ("Power Plant 8D",8,"D",27.0,80,6021720),\
    "PP 8C": ("Power Plant 8C",8,"C",30.0,85,18065170),\
    "PP 8B": ("Power Plant 8B",8,"B",33.0,85,54195500),\
    "PP 8A": ("Power Plant 8A",8,"A",36.0,90,162586490)
    }

THUSTERS = {"TH 2E": ("Thruster 2E","2","E",2,20,[],1980),\
    "TH 2D": ("Thruster 2D",2,"D",2.25,20,[Effect("speed",1)],5930),\
    "TH 2C": ("Thruster 2C",2,"C",2.5,25,[Effect("speed",1),Effect("agility",1)],17800),\
    "TH 2B": ("Thruster 2B",2,"B",2.75,25,[Effect("speed",2),Effect("agility",1)],53410),\
    "TH 2A": ("Thruster 2A",2,"A",3.0,30,[Effect("speed",2),Effect("agility",2)],160220),\
    "TH 3E": ("Thruster 3E",3,"E",2.48,30,[],6270),\
    "TH 3D": ("Thruster 3D",3,"D",2.79,30,[Effect("speed",1)],18810),\
    "TH 3C": ("Thruster 3C",3,"C",3.1,35,[Effect("speed",1),Effect("agility",1)],56440),\
    "TH 3B": ("Thruster 3B",3,"B",3.41,35,[Effect("speed",2),Effect("agility",1)],169300),\
    "TH 3A": ("Thruster 3A",3,"A",3.72,40,[Effect("speed",2),Effect("agility",2)],507910),\
    "TH 4E": ("Thruster 4E",4,"E",3.82,40,[],19880),\
    "TH 4D": ("Thruster 4D",4,"D",3.69,40,[Effect("speed",1)],56630),\
    "TH 4C": ("Thruster 4C",4,"C",4.1,45,[Effect("speed",1), Effect("agility",1)],178900),\
    "TH 4B": ("Thruster 4B",4,"B",4.51,45,[Effect("speed",2),Effect("agility",1)],536690),\
    "TH 4A": ("Thruster 4A",4,"A",4.92,50,[Effect("speed",2),Effect("agility",2)],1610080),\
    "TH 5E": ("Thruster 5E",5,"E",4.08,50,[],63010),\
    "TH 5D": ("Thruster 5D",5,"D",4.59,50,[Effect("speed",1)],189040),\
    "TH 5C": ("Thruster 5C",5,"C",5.1,55,[Effect("speed",1), Effect("agility",1)],567110),\
    "TH 5B": ("Thruster 5B",5,"B",5.61,55,[Effect("speed",2),Effect("agility",1)],1701320),\
    "TH 5A": ("Thruster 5A",5,"A",6.12,60,[Effect("speed",2),Effect("agility",2)],5103950),\
    "TH 6E": ("Thruster 6E",6,"E",5.04,60,[],199750),\
    "TH 6D": ("Thruster 6D",6,"D",5.67,60,[Effect("speed",1)],599240),\
    "TH 6C": ("Thruster 6C",6,"C",6.3,65,[Effect("speed",1), Effect("agility",1)],1797730),\
    "TH 6B": ("Thruster 6B",6,"B",6.93,65,[Effect("speed",2),Effect("agility",1)],5393180),\
    "TH 6A": ("Thruster 6A",6,"A",7.56,70,[Effect("speed",2),Effect("agility",2)],16179530),\
    "TH 7E": ("Thruster 7E",7,"E",6.08,70,[],633200),\
    "TH 7D": ("Thruster 7D",7,"D",6.84,70,[Effect("speed",1)],1899600),\
    "TH 7C": ("Thruster 7C",7,"C",7.6,75,[Effect("speed",1), Effect("agility",1)],5698790),\
    "TH 7B": ("Thruster 7B",7,"B",8.36,75,[Effect("speed",2),Effect("agility",1)],17096370),\
    "TH 7A": ("Thruster 7A",7,"A",9.12,80,[Effect("speed",2),Effect("agility",2)],51289110),\
    "TH 8E": ("Thruster 8E",8,"E",7.2,80,[],2007240),\
    "TH 8D": ("Thruster 8D",8,"D",8.1,80,[Effect("speed",1)],6021720),\
    "TH 8C": ("Thruster 8C",8,"C",9.0,85,[Effect("speed",1), Effect("agility",1)],18065170),\
    "TH 8B": ("Thruster 8B",8,"B",9.9,85,[Effect("speed",2),Effect("agility",1)],54195500),\
    "TH 8A": ("Thruster 8A",8,"A",10.8,90,[Effect("speed",2),Effect("agility",2)],162586500),\
    }

FSD = {"fsd 2E": ("Frame Shift Drive 2E",2,"E",0.16,15,7,1980),\
    "fsd 2D": ("Frame Shift Drive 2D",2,"D",0.18,15,8,5930),\
    "fsd 2C": ("Frame Shift Drive 2C",2,"C",0.2,20,10,17800),\
    "fsd 2B": ("Frame Shift Drive 2B",2,"B",0.25,20,11,53410),\
    "fsd 2A": ("Frame Shift Drive 2A",2,"A",0.3,25,13,160220),\
    "fsd 3E": ("Frame Shift Drive 3E",3,"E",0.24,25,9,6270),\
    "fsd 3D": ("Frame Shift Drive 3D",3,"D",0.27,25,10,18810),\
    "fsd 3C": ("Frame Shift Drive 3C",3,"C",0.3,30,12,56440),\
    "fsd 3B": ("Frame Shift Drive 3B",3,"B",0.38,30,13,169300),\
    "fsd 3A": ("Frame Shift Drive 3A",3,"A",0.45,35,15,507910),\
    "fsd 4E": ("Frame Shift Drive 4E",4,"E",0.24,35,11,19880),\
    "fsd 4D": ("Frame Shift Drive 4D",4,"D",0.27,35,12,59630),\
    "fsd 4C": ("Frame Shift Drive 4C",4,"C",0.3,40,14,178900),\
    "fsd 4B": ("Frame Shift Drive 4B",4,"B",0.38,40,15,536690),\
    "fsd 4A": ("Frame Shift Drive 4A",4,"A",0.45,45,17,1610080),\
    "fsd 5E": ("Frame Shift Drive 5E",5,"E",0.32,45,13,63010),\
    "fsd 5D": ("Frame Shift Drive 5D",5,"D",0.36,45,14,189040),\
    "fsd 5C": ("Frame Shift Drive 5C",5,"C",0.4,50,16,567110),\
    "fsd 5B": ("Frame Shift Drive 5B",5,"B",0.5,50,17,1701320),\
    "fsd 5A": ("Frame Shift Drive 5A",5,"A",0.6,55,19,5103950),\
    "fsd 6E": ("Frame Shift Drive 6E",6,"E",0.4,55,15,199750),\
    "fsd 6D": ("Frame Shift Drive 6D",6,"D",0.45,55,16,599240),\
    "fsd 6C": ("Frame Shift Drive 6C",6,"C",0.5,60,18,1797730),\
    "fsd 6B": ("Frame Shift Drive 6B",6,"B",0.63,60,19,5393180),\
    "fsd 6A": ("Frame Shift Drive 6A",6,"A",0.75,65,21,16179530),\
    "fsd 7E": ("Frame Shift Drive 7E",7,"E",0.48,65,17,633200),\
    "fsd 7D": ("Frame Shift Drive 7D",7,"D",0.54,65,18,1899600),\
    "fsd 7C": ("Frame Shift Drive 7C",7,"C",0.6,70,20,5698800),\
    "fsd 7B": ("Frame Shift Drive 7B",7,"B",0.75,70,21,17096380),\
    "fsd 7A": ("Frame Shift Drive 7A",7,"A",0.9,75,23,51289120),\
    "fsd 8E": ("Frame Shift Drive 8E",8,"E",0.6,75,19,2007240),\
    "fsd 8D": ("Frame Shift Drive 8D",8,"D",0.73,75,20,6021720),\
    "fsd 8C": ("Frame Shift Drive 8C",8,"C",0.88,80,22,18065170),\
    "fsd 8B": ("Frame Shift Drive 8B",8,"B",0.95,80,23,54195500),\
    "fsd 8A": ("Frame Shift Drive 8A",8,"A",1.05,85,25,162586500)
    }

LIFE_SUPPORT = {"ls 1E":("Life support 1E",1,"E",0.32,15,"5m",520),\
    "ls 1D":("Life support 1D",1,"D",0.36,15,"7m 30s",1290),\
    "ls 1C":("Life support 1C",1,"C",0.4,20,"10m",3230),\
    "ls 1B":("Life support 1B",1,"B",0.44,20,"15m",8080),\
    "ls 1A":("Life support 1A",1,"A",0.48,25,"25m",20200),\
    "ls 2E":("Life support 2E",2,"E",0.37,25,"5m",1450),\
    "ls 2D":("Life support 2D",2,"D",0.41,25,"7m 30s",3620),\
    "ls 2C":("Life support 2C",2,"C",0.46,30,"10m",9050),\
    "ls 2B":("Life support 2B",2,"B",0.51,30,"15m",22620),\
    "ls 2A":("Life support 2A",2,"A",0.55,35,"25m",56550),\
    "ls 3E":("Life support 3E",3,"E",0.42,35,"5m",4050),\
    "ls 3D":("Life support 3D",3,"D",0.48,35,"7m 30s",10130),\
    "ls 3C":("Life support 3C",3,"C",0.53,40,"10m",25330),\
    "ls 3B":("Life support 3B",3,"B",0.58,40,"15m",63330),\
    "ls 3A":("Life support 3A",3,"A",0.64,45,"25m",158330),\
    "ls 4E":("Life support 4E",4,"E",0.5,45,"5m",11350),\
    "ls 4D":("Life support 4D",4,"D",0.56,45,"7m 30s",28370),\
    "ls 4C":("Life support 4C",4,"C",0.62,50,"10m",70930),\
    "ls 4B":("Life support 4B",4,"B",0.68,50,"15m",177330),\
    "ls 4A":("Life support 4A",4,"A",0.74,55,"25m",443330),\
    "ls 5E":("Life support 5E",5,"E",0.57,55,"5m",31780),\
    "ls 5D":("Life support 5D",5,"D",0.64,55,"7m 30s",79440),\
    "ls 5C":("Life support 5C",5,"C",0.71,60,"10m",198610),\
    "ls 5B":("Life support 5B",5,"B",0.78,60,"15m",496530),\
    "ls 5A":("Life support 5A",5,"A",0.85,65,"25m",1241320),\
    "ls 6E":("Life support 6E",6,"E",0.64,65,"5m",88980),\
    "ls 6D":("Life support 6D",6,"D",0.72,65,"7m 30s",222440),\
    "ls 6C":("Life support 6C",6,"C",0.8,70,"10m",556110),\
    "ls 6B":("Life support 6B",6,"B",0.88,70,"15m",1390280),\
    "ls 6A":("Life support 6A",6,"A",0.96,75,"25m",3475690),\
    "ls 7E":("Life support 7E",7,"E",0.72,75,"5m",249140),\
    "ls 7D":("Life support 7D",7,"D",0.81,75,"7m 30s",622840),\
    "ls 7C":("Life support 7C",7,"C",0.9,80,"10m",1557110),\
    "ls 7B":("Life support 7B",7,"B",0.99,80,"15m",3892770),\
    "ls 7A":("Life support 7A",7,"A",1.08,85,"25m",9731930),\
    "ls 8E":("Life support 8E",8,"E",0.8,85,"5m",697590),\
    "ls 8D":("Life support 8D",8,"D",0.9,85,"7m 30s",1743970),\
    "ls 8C":("Life support 8C",8,"C",1,90,"10m",4359900),\
    "ls 8B":("Life support 8B",8,"B",1.1,90,"15m",10899770),\
    "ls 8A":("Life support 8A",8,"A",1.2,95,"25m",27249400),\
    }

POWER_DIST = {'pd 1E':('Power Distribution 1E',1,'E',0.32,10,[],520),\
    'pd 1D':('Power Distribution 1D',1,'D',0.36,10,[Effect("float_pts",1)],1290),\
    'pd 1C':('Power Distribution 1C',1,'C',0.4,15,[Effect("float_pts",2)],3230),\
    'pd 1B':('Power Distribution 1B',1,'B',0.44,15,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],8080),\
    'pd 1A':('Power Distribution 1A',1,'A',0.48,20,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],20200),\
    'pd 2E':('Power Distribution 2E',2,'E',0.36,20,[],1450),\
    'pd 2D':('Power Distribution 2D',2,'D',0.41,20,[Effect("float_pts",1)],3620),\
    'pd 2C':('Power Distribution 2C',2,'C',0.45,25,[Effect("float_pts",2)],9050),\
    'pd 2B':('Power Distribution 2B',2,'B',0.5,25,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],22620),\
    'pd 2A':('Power Distribution 2A',2,'A',0.54,30,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],56550),\
    'pd 3E':('Power Distribution 3E',3,'E',0.4,30,[],4050),\
    'pd 3D':('Power Distribution 3D',3,'D',0.45,30,[Effect("float_pts",1)],10130),\
    'pd 3C':('Power Distribution 3C',3,'C',0.5,35,[Effect("float_pts",2)],25330),\
    'pd 3B':('Power Distribution 3B',3,'B',0.55,35,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],63330),\
    'pd 3A':('Power Distribution 3A',3,'A',0.6,40,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],158330),\
    'pd 4E':('Power Distribution 4E',4,'E',0.45,40,[],11350),\
    'pd 4D':('Power Distribution 4D',4,'D',0.5,40,[Effect("float_pts",1)],28370),\
    'pd 4C':('Power Distribution 4C',4,'C',0.56,45,[Effect("float_pts",2)],70930),\
    'pd 4B':('Power Distribution 4B',4,'B',0.62,45,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],177330),\
    'pd 4A':('Power Distribution 4A',4,'A',0.67,50,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],443330),\
    'pd 5E':('Power Distribution 5E',5,'E',0.5,50,[],31780),\
    'pd 5D':('Power Distribution 5D',5,'D',0.56,50,[Effect("float_pts",1)],79440),\
    'pd 5C':('Power Distribution 5C',5,'C',0.62,55,[Effect("float_pts",2)],198610),\
    'pd 5B':('Power Distribution 5B',5,'B',0.68,55,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],496530),\
    'pd 5A':('Power Distribution 5A',5,'A',0.74,60,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],1241320),\
    'pd 6E':('Power Distribution 6E',6,'E',0.54,60,[],88980),\
    'pd 6D':('Power Distribution 6D',6,'D',0.61,60,[Effect("float_pts",1)],222440),\
    'pd 6C':('Power Distribution 6C',6,'C',0.68,65,[Effect("float_pts",2)],556110),\
    'pd 6B':('Power Distribution 6B',6,'B',0.75,65,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],1390280),\
    'pd 6A':('Power Distribution 6A',6,'A',0.82,70,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],3475690),\
    'pd 7E':('Power Distribution 7E',7,'E',0.59,70,[],249140),\
    'pd 7D':('Power Distribution 7D',7,'D',0.67,70,[Effect("float_pts",1)],622840),\
    'pd 7C':('Power Distribution 7C',7,'C',0.74,75,[Effect("float_pts",2)],1557110),\
    'pd 7B':('Power Distribution 7B',7,'B',0.81,75,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],3892770),\
    'pd 7A':('Power Distribution 7A',7,'A',0.89,80,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],9731930),\
    'pd 8E':('Power Distribution 8E',8,'E',0.64,80,[],697580),\
    'pd 8D':('Power Distribution 8D',8,'D',0.72,80,[Effect("float_pts",1)],1743960),\
    'pd 8C':('Power Distribution 8C',8,'C',0.8,85,[Effect("float_pts",2)],4359900),\
    'pd 8B':('Power Distribution 8B',8,'B',0.88,85,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5)],10899760),\
    'pd 8A':('Power Distribution 8A',8,'A',0.96,90,[Effect("agility", 1), Effect("to_hit",1), Effect("shield_recharge",5),Effect("float_pts",1)],27249390),\
    }

SENSORS = {'ss1E':('Sensors 1E',1,'E',0.16,5,[],520),\
    'ss1D':('Sensors 1D',1,'D',0.18,5,[Effect('initiative',1)],1290),\
    'ss1C':('Sensors 1C',1,'C',0.2,10,[Effect('initiative',1),Effect('dogfghting',1)],3230),\
    'ss1B':('Sensors 1B',1,'B',0.33,10,[Effect('initiative',2),Effect('dogfghting',1)],8080),\
    'ss1A':('Sensors 1A',1,'A',0.6,15,[Effect('initiative',2),Effect('dogfghting',2)],20200),\
    
    'ss2E':('Sensors 2E',2,'E',0.18,15,[Effect('sensors',1)],1450),\
    'ss2D':('Sensors 2D',2,'D',0.21,15,[Effect('initiative',1),Effect('sensors',1)],3620),\
    'ss2C':('Sensors 2C',2,'C',0.23,20,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',1)],9050),\
    'ss2B':('Sensors 2B',2,'B',0.38,20,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',1)],22620),\
    'ss2A':('Sensors 2A',2,'A',0.69,25,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',1)],56550),\
    
    'ss3E':('Sensors 3E',3,'E',0.22,25,[Effect('sensors',1)],4050),\
    'ss3D':('Sensors 3D',3,'D',0.25,25,[Effect('initiative',1),Effect('sensors',1)],10130),\
    'ss3C':('Sensors 3C',3,'C',0.28,30,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',1)],25330),\
    'ss3B':('Sensors 3B',3,'B',0.46,30,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',1)],63330),\
    'ss3A':('Sensors 3A',3,'A',0.84,35,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',1)],158330),\
    
    'ss4E':('Sensors 4E',4,'E',0.27,35,[Effect('sensors',2)],11350),\
    'ss4D':('Sensors 4D',4,'D',0.31,35,[Effect('initiative',1),Effect('sensors',2)],28370),\
    'ss4C':('Sensors 4C',4,'C',0.34,40,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',2)],70930),\
    'ss4B':('Sensors 4B',4,'B',0.56,40,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',2)],177330),\
    'ss4A':('Sensors 4A',4,'A',1.02,45,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',2)],443330),\
    
    'ss5E':('Sensors 5E',5,'E',0.33,45,[Effect('sensors',3)],31780),\
    'ss5D':('Sensors 5D',5,'D',0.37,45,[Effect('initiative',1),Effect('sensors',3)],79440),\
    'ss5C':('Sensors 5C',5,'C',0.41,50,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',3)],198610),\
    'ss5B':('Sensors 5B',5,'B',0.68,50,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',3)],496530),\
    'ss5A':('Sensors 5A',5,'A',1.23,55,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',3)],1241320),\
    
    'ss6E':('Sensors 6E',6,'E',0.4,55,[Effect('sensors',3)],88980),\
    'ss6D':('Sensors 6D',6,'D',0.45,55,[Effect('initiative',1),Effect('sensors',3)],222440),\
    'ss6C':('Sensors 6C',6,'C',0.5,60,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',3)],556110),\
    'ss6B':('Sensors 6B',6,'B',0.83,60,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',3)],1390280),\
    'ss6A':('Sensors 6A',6,'A',1.5,65,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',3)],3475690),\
    
    'ss7E':('Sensors 7E',7,'E',0.47,65,[Effect('sensors',4)],249140),\
    'ss7D':('Sensors 7D',7,'D',0.53,65,[Effect('initiative',1),Effect('sensors',4)],622840),\
    'ss7C':('Sensors 7C',7,'C',0.59,70,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',4)],1557110),\
    'ss7B':('Sensors 7B',7,'B',0.97,70,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',4)],3892770),\
    'ss7A':('Sensors 7A',7,'A',1.77,75,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',4)],9731930),\
    
    'ss8E':('Sensors 8E',8,'E',0.55,75,[Effect('sensors',5)],697580),\
    'ss8D':('Sensors 8D',8,'D',0.62,75,[Effect('initiative',1),Effect('sensors',5)],1743960),\
    'ss8C':('Sensors 8C',8,'C',0.69,80,[Effect('initiative',1),Effect('dogfghting',1),Effect('sensors',5)],4359900),\
    'ss8B':('Sensors 8B',8,'B',1.14,80,[Effect('initiative',2),Effect('dogfghting',1),Effect('sensors',5)],10899760),\
    'ss8A':('Sensors 8A',8,'A',2.07,85,[Effect('initiative',2),Effect('dogfghting',2),Effect('sensors',5)],27249390),\
    }

FUEL_TANK = {"ft 1C":("Fuel Tank 1C",1,2,1000),\
    "ft 2C":("Fuel Tank 2C",2,4,3750),\
    "ft 3C":("Fuel Tank 3C",3,8,7060),\
    "ft 4C":("Fuel Tank 4C",4,16,24730),\
    "ft 5C":("Fuel Tank 5C",5,32,97750),\
    "ft 6C":("Fuel Tank 6C",6,64,341580),\
    "ft 7C":("Fuel Tank 7C",7,128,1780910),\
    "ft 8C":("Fuel Tank 8C",8,256,5428400)
    }

BACKGROUNDS = {'acco':('Accountant',1,[Effect('bluff',10),Effect('comp',10),Effect('cult_law',20),Effect('dodge',10)],'N/A','N/A','You were brought up in a shadowy world of balance sheets, credit notes, purchase ledgers and taxdeductible lunches. Since computers are used for honest tax statements, human accountants exist only to tease, stretch and reimagine tax law to provide exemptions for their clients. After years of dodging the tax authorities you were glad to pack it all in and become something safer - like a pirate or bounty hunter.'),\
    'anar':('Anarchist',1,[Effect('dodge',10),Effect('fight',10),Effect('grenade',20),Effect('intim',10)],'N/A','N/A','The super-rich, corporate leaders and their stooge politicians, have the whole of society stitched up and the very concept of freedom is a joke. As a young person you threw rocks through police-station windows, belched at local dignitaries, assaulted corporate management and spent years in a variety of prisons.'),\
    'army':('Army Trained',2,[Effect('dodge',10),Effect('eng_weap',20),Effect('fight',10),Effect('grenade',10),Effect('hvy_weap',10),Effect('kin_weap',20),Effect('med',10),Effect('veh_weap',10)],'N/A','N/A','You are a fully trained infantry soldier for one of the three great powers, Federation, Empire or Alliance. Your comprehensive military training covered all aspects of modern warfare and you are an accurate and deadly opponent in personal combat.'),\
    'big':('Big Game Hunter',1,[Effect('kin_weap',10),Effect('stealth',20),Effect('surv',20)],'N/A','N/A','Some people only feel big when shooting defenceless animals at extreme range with advanced weaponry.  For a minority, however, the real challenge comes from shooting animals that could rip your face off at extreme range with advanced weaponry.  Naturally, anyone who intends to bag anything bigger than a Borchuck isn’t going to fight fair, and neither do you.  Quiet, deadly, and with your own code of honour that doesn’t include animal rights, you are the bane of deadly predators everywhere.  Get down the Rail Rifle – it’s time to go duck hunting!'),\
    'bord':('Borderland Homeworld',1,[Effect('dodge',10),Effect('fight',10),Effect('kin_weap',10),Effect('repair',10),Effect('surv',10)],'N/A','N/A','You were brought up on the frontier, on a planet of lowlifes and criminals. Such a society breeds tough people and you are no exception.'),\
    'born':('Born On The Streets',1,[Effect('stealth',10),Effect('strwise',20)],['tough'],'N/A','You are an orphan and have spent a good proportion of your life on the streets of some megacity, scrounging for scraps and stealing just to stay alive. Your experience has made you tough, plain speaking and sneaky.'),\
    'box':('Boxer',1,[Effect('fight',20),Effect('parry',10)],['strong'],'N/A','You are a professionally trained boxer, although you never made it to the big time. You have a mean right hook and you’re as strong as they come.'),\
    'cast':('Castaway',1,[Effect('mel_weap',10),Effect('surv',20)],['surivialist'],'N/A','You were stranded on a distant earth-like world for more than a decade, and had to survive using basic tools and ingenuity.  You never expected to be rescued, and now you are back in civilisation, and with all the noise and fury of modern living you feel a little lost.  The wilderness calls to you again, and you know that your destiny lies amongst the mysterious and ancient stars of distant worlds.'),\
    'cheer':('Cheerleader',1,[Effect('athlet',20),Effect('charm',10),Effect('sleight',10),Effect('stealth',10)],'N/A','N/A','Your planet worships sports heroes, and as a young person you joined one of the thousands of cheerleading teams with a patriotic fervour. The cheerleading team was rife with ambition, intrigue and an obsession with physical perfection, and you got up to many japes and schemes during your time in the corp.'),\
    'child':('Child Actor',1,[Effect('bluff',20),Effect('dip',20),Effect('mel_weap',10)],'N/A','N/A','Your pushy parents forced you into an endless series of humiliating auditions since you were a baby. You’ve been through the works; the drugs, the hangers-on, the sycophants – you’ve even done some acting. After years of over-entitlement and crushing depression you’ve emerged from the darkness of youth into the damaged, ambitious person you are today.'),\
    'comm':('Community Youth Worker',1,[Effect('insight',20),Effect('kin_weap',10),Effect('parry',10),Effect('strwise',10)],'N/A','N/A','The young of the galaxy are often exposed to suffocating levels of overexpectation, including nearly limitless examinations, detailed scouring on social media and almost fatal levels of subliminal toy advertising. Small wonder that more than a few end up as near psychopathic wrecks. It takes a special kind of person to be a Community Youth Worker, a combination of empathy, masochism and speed of reaction is necessary to see the year out.'),\
    'corp':('Corporate Security ',1,[Effect('dodge',10),Effect('eng_weap',10),Effect('fight',10),Effect('sec',20)],'N/A','N/A','The private military forces of the corporations vary hugely, between the advanced, highly regimented navies of Sirius to the overbearing thugs of the Achilles Corporation.  Regardless, it is the job of Corporate Security to lay down their lives for the company, to be the blood and muscle shield between them and the seething masses of the public.  Security guards vary, somewhat, in their levels of loyalty, but all are trained in security measures, restraining intruders, and bullying staff who take too long in the toilet.'),\
    'crim':('Criminal Family',1,[Effect('bluff',10),Effect('charm',10),Effect('gambling',10),Effect('sec',10),Effect('stealth',10)],'N/A','N/A','You were born into a glorious heritage of utterly corrupt criminality. Your mother and father were gangsters, possibly gangster lords. All your family are part of the ‘family’, and it is expected that you too will help the business once you’ve got this space adventuring lark out of your system. As a member of the criminal elite you are not expected to get involved with all that rough stuff. Lying, seducing and stealing are more your kind of skills.'),\
    'cybo':('Cyborg',1,[],'N/A','Start with 100,000 credits worth of Cybernetics','You are part machine and part human - and not in a subtle way; in a big, clanking half robot kind of way. Most people who end up like this suffered terrible injuries and did not have the money for genetic limb replacement. A few mercenary and criminal types actually volunteer for this horrifying surgery, believing it makes them look intimidating. They might be right.'),\
    'disg':('Disgraced Banker',1,[Effect('dodge',10),Effect('eng_weap',10),Effect('tact',10),Effect('trade',20)],'N/A','N/A','Successful banks take risks, and expect their employees to do the same. When an employee ‘screws up’ (i.e. loses the bank a lot of money), the bank will sack them in disgrace for taking exactly the kind of risk they have been expected to take. These rules are well understood in the banking and stock market community, but that didn’t make it any less painful when the bank dumped you and began co-operating with the police to stitch you up. Escaping the cops has been an education in itself. Lucky you stashed away a cheap ship just in case this sort of thing happened…'),\
    'dock':('Docking Bay Operative',1,[Effect('nav',10),Effect('plant_know',10),Effect('repair',10),Effect('sec',10),Effect('trade',10)],'N/A','N/A','You work in a low-gravity environment on a large space station, such as a Coriolis or Ocellus space dock. You have looked after Docking Bay 42 for years, watching as idiots with half your skill and training crash land onto your pristine landing pad. You’ve seen the swaggering arrogance of those spaceship commanders. With your real Skills as a docking bay operative you’ll be outmanoeuvring pirates and shooting down space terrorists in no time!'),\
    'drone':('Drone Controller',1,[Effect('comp',10),Effect('cyber',20)],'N/A','You begin with a T-90 Patrol Drone','The best way to fight is to be nowhere near the enemy. Drones are the ultimate expression of that philosophy. Some call drone controllers cowards. You prefer to call yourself a realist. Your favourite battlefield is a coffee cup strewn desktop, a slate computer in one hand, a Chef burger in the other, watching as your Walker Drone pounds street punks into a bloody mess. The only real challenge of the battle is afterwards, when you have to wobble out of your armchair to get to the toilet.'),\
    'engin':('Engineer',1,[Effect('comp',10),Effect('cyber',10),Effect('eng_weap',10),Effect('repair',20)],'N/A','N/A','You are a highly qualified technical engineer with a solid grasp of the latest technology. Your skills are in high demand across the galaxy and there is very little you cannot fix or reprogram. Being able to repair your own ship greatly reduces costs, and makes you a lifesaver in any group you care to join.'),\
    'expl':('Explorer Corp',1,[Effect('nav',20),Effect('plant_know',10),Effect('surv',10),Effect('veh_plt',10)],'N/A','N/A','The lure of deep space beckons to the bold. Fabulous hidden riches await those with the guts to venture beyond the bubble of human occupied space. As an explorer you are expert in navigation and survival. There is nothing you like better than landing on a pristine alien world and to churn up the earth as you speed around in your eight-wheeled SRV.'),\
    'fede':('Federal Reservist',1,[Effect('dodge',10),Effect('fight',10),Effect('intim',10),Effect('kin_weap',10),Effect('stealth',10)],'N/A','N/A','The Federation military is constantly planning for the war to end all wars – a direct confrontation with the Imperial navy. The trouble is they don’t want to pay for it, at least not all the time.  Rather than have billions of troops on constant standby, the Federation runs a volunteer military program for patriotic reservists.  Such men and women are wannabe soldiers, either unfit for full service or too bound to civilian life to be willing to devote their entire lives to the cause.  Some reservists are quiet patriots who patiently wait for their nation to call them up.  Others will never cease to remind their friends and neighbours that they are fully-trained soldiers, even going so far as to wear their uniform off duty.'),\
    'figh':('Fighter Pilot',1,[Effect('ship_plt',10),Effect('ship_weap',10),Effect('sys',20),Effect('tact',10)],'N/A','N/A','In addition to your basic training you have received advanced training to fly a combat spaceship, such as a Viper or Eagle. You served in an elite fighter corp, either as part of a formal navy or, more likely, as part of a planetary defence force. Your quick reactions make you one of the best space warriors in the galaxy.'),\
    'free':('Freedom Fighter',1,[Effect('dodge',10),Effect('eng_weap',10),Effect('grenade',10),Effect('stealth',10),Effect('veh_plt',10)],'N/A','N/A','Across the galaxy tyranny and dictatorship are in good shape, with petty despots lording it over their frightened and bullied population. You were part of a band of fighters that stood up to this oppression using stealth, resourcefulness or good old fashioned grit. Perhaps you were successful and your planet is now free, or maybe your band was hunted down and you are the last survivor. Either way it is time to move on with your life.'),\
    'front':('Frontier Trader',1,[Effect('bargin',10),Effect('dodge',10),Effect('kin_weap',10),Effect('trade',20)],'N/A','N/A','You worked on a small trading ship, selling desperately needed goods to the poorest folk on the frontier. Many of those places are ridden with anarchy or spirit crushing autocracies, and you had to fight to survive when petty criminals or corrupt tax inspectors came to shake you down. Now you own your own ship. With your extensive trading experience it’s time to earn some real money!'),\
    'fuel':('Fuel Rat',1,[Effect('nav',20),Effect('plant_know',10),Effect('ship_plt',10),Effect('trade',10)],'N/A','N/A','The Fuel Rats are a charitable organisation that rescues stranded pilots who accidentally use up all their fuel supplies. Sometimes derided by pilots who claim the Fuel Rats have too much time on their hands, no one forgets the moment a noble Fuel Rat saves them from certain death in the cold depths of space. You are an ex-ratter, and as a consequence feel a strong bond with your fellow pilots crawling through the depths of space. Still, it doesn’t pay the bills, so now it’s time to go out and earn some credits!'),\
    'gene':('Gene Mod Baby',1,[],'N/A',[Empty(),Empty()],'It is illegal in most societies to subject children to extensive, non-medical genetic manipulation. But there are loopholes, especially for the children of the rich. You were one such child, given a leg-up by your parents over your brutish and ape-like contemporaries. Many such children end up insane or hopelessly obsessional, but you are one of the lucky ones. You are simply better than other people although you try to conceal your contempt behind your fidgeting, manic stare.'),\
    'gym ':('Gym Freak',1,[Effect('athlet',10)],['quick runner','strong'],'N/A','It started out as a simple way to get fit. After New Year’s Feast you felt all flabby and exhausted. These days it takes a 20k run to break a sweat on you, and you have the kind of body Greek gods would be envious of. You are a helpless workout addict, twice as much now you work in zero gravity. Can’t let those low G’s impact on your perfect body now, can we?'),\
    'hack':('Hacker',1,[Effect('comp',20),Effect('sec',10)],['natural genius (computer)'],'N/A',"You are AvEn6eR_99, little less than a digital god. The witless people of your home world are sheep for you to fatten and crush (that’s what you do with sheep, isn’t it?). The authorities cannot catch you because you live constantly on the run, using the police force’s own servers to hack extra credit onto your Sunbuck coffee card and claiming hotel rooms as expenses for the police commissioner. You giggled as you released top secrets from the security services data farms from the comfort of some flea-ridden hotel on your three-year-old handheld com. Then one day you realised that you were nothing more than a homeless coffee addict, and the people you stole from lived in large mansions attended by servants. You decided they had the right idea, so now it’s time to make your skills pay."),\
    'high':('High Tech Homeworld',1,[Effect('comp',10),Effect('cyber',10),Effect('eng_weap',10),Effect('sci',10),Effect('sys',10)],'N/A','N/A','You lived on a technologically advanced planet where almost every conceivable human need could be assisted by robots, computers and machines. Technology suffuses your thoughts and actions, and even ordering a coffee on this planet is a complex social and technical puzzle for outsiders. You cannot help, growing up in such a place, becoming intimately familiar with all the trappings of the modern galaxy.'),\
    'hoop':('Hoopy Casino Croupier',1,[Effect('gambling',20),Effect('perc',10),Effect('sleight',20)],'N/A','N/A','The fortunes of Hoopy’s Casinos has risen and fallen across three centuries, but the galaxy’s favourite provider of fortune-sapping entertainment has never entirely disappeared. One of your first jobs was in these glamorous gambling halls, keeping an eye on the mega-roulette wheel. It was not an honest job. The casino had you bounce and shuffle the roulette ball to ensure limited wins, and you had to keep an eye out for customers who wished to game the system.'),\
    'insu':('Insurgent',1,[Effect('bluff',20),Effect('fight',10),Effect('sec',10),Effect('stealth',10)],'N/A','N/A','You were an anti-capitalist spy, who specialised in infiltrating organisations to either bring them down or cause them irreparable harm. Insurgents are often former wage slaves who bear a heavy grudge against the company that once employed them.  The difference between being an insurgent and a freedom fighter is that you mostly work alone – the company will be scanning all your communications, so you must follow your own code and instincts as you strike against them.  Insurgents can be pranksters or violent terrorists, and are particularly common (and despised) in the Federation, where companies have near carte blanche to act as they please.'),\
    'labor':('Labour Slave',1,[Effect('fight',10)],['strong','tough'],'N/A','You are an escaped slave who was condemned to perform back-breaking labour. You might be a disillusioned Imperial citizen enslaved for debts, or a poor frontier civilian captured by slaver gangs such as the Kumo Crew. Your treatment has been appalling and degrading, and to escape you have taken lives with your bare hands. One day you might be able to bring yourself to talk about it, but for the moment you keep your eyes forward and the past far behind, staving off sleep for days at a time with caffeine pills and stimulants. '),\
    'lave':('Lave Radio Host',1,[Effect('bluff',20),Effect('charm',10),Effect('insight',20)],'N/A','N/A','Lave Radio is at the forefront of a movement in news media that sees the replacement of old fashioned investigatory journalism with vague guesses, assumptions and a gutsy determination to fill ‘dead air’. You were a presenter of this show, or one very like it, and have become adept at wild speculation and inferring the big picture from a few lines of text.'),\
    'mart':('Martial Artist',2,[Effect('athlet',20),Effect('dodge',20),Effect('fight',20),Effect('mel_weap',20),Effect('parry',20)],'N/A','N/A','You have been extensively trained in unarmed and melee combat which has turned your body into a lethal weapon. You are physically fit and have quick reflexes having been in training since you were a child. A number of secret organisations value the martial arts, especially those who work in places where carrying guns is difficult if not impossible.'),\
    'merc':('Mercenary',2,[Effect('dodge',20),Effect('fight',10),Effect('hvy_weap',20),Effect('kin_weap',10),Effect('tact',10),Effect('veh_weap',10)],'tough','N/A','You have served in a rough, semi-legal profession that kills for money. Your mercenary outfit specialised in ground combat, especially in the use of heavy weapons. Lacking any kind of subtlety, your unit used brute force to accomplish its aims. Anyone working for such an organisation needs to be tough and hard edged to live more than a few days.'),\
    'mili':('Military Courier',1,[Effect('bluff',10),Effect('nav',10),Effect('ship_plt',10),Effect('veh_plt',10),Effect('veh_weap',10)],'N/A','N/A','Everyone uses the network to communicate.  It links separate star systems, connects cities and people, and lets you talk, flirt and threaten your way across the galaxy.  Of course, it’s hopelessly compromised.  Everyone is listening, and agents of the various powers scour every word for potential espionage, criminal or blackmail material.  The militaries of all the great powers only use the network for the most routine communications.  All other messages are sent in person, by ship or bike, directly to the receiver.  Getting in on this action is good, steady work, although it can be dangerous.  The messages you are transporting carry great value and the risk of being intercepted by enemy agents always lingers in the background.'),\
    'mine':('Mining Engineer',1,[Effect('grenade',10),Effect('hvy_weap',20),Effect('repair',10),Effect('sys',10)],'N/A','N/A','You were a Borderworld strip-miner, employed by a profit hungry corporation such as Mastopolos or Caine Massey. Strip mining involves little subtlety. Heavy barrage mining tools, little more than colossal hand-held rocket launchers, are used to blast away the bedrock, and the resulting rubble is processed by the ton through gigantic sifters. Entire mountain ranges are levelled to produce the ore the galaxy demands.'),\
    'poli':('Minor Politician',1,[Effect('bargin',10),Effect('cult_law',10),Effect('dip',10),Effect('perc',10),Effect('tact',10)],'N/A','N/A','You have served as a minor official on a planet or space station. Depending on where you were born you might have been elected or appointed to this role. Either way you have had to deal with petty bureaucracies and troublesome citizens as you navigated the quagmire of government. You understand people and law well, and know when to act and when to conveniently be missing from the room.'),\
    'monk':('Monk/Nun',1,[Effect('fight',10),Effect('insight',20),Effect('med',10),Effect('stealth',10)],'N/A','N/A','You were a member of a religious order such as Utopian Vision or an old Earth faith that placed many demands and restrictions upon your activities, behaviour and freedom. In order to achieve a higher level of spiritual awareness you have fasted, meditated in aching loneliness, and prayed for many days on end. You have left that life behind now, but your time has not been wasted; you have picked up many skills from your spiritual journey.'),\
    'navy':('Navy Trained',2,[Effect('dodge',10),Effect('eng_weap',10),Effect('fight',10),Effect('repair',20),Effect('sec',10),Effect('ship_plt',10),Effect('ship_weap',10),Effect('sys',20)],'N/A','N/A','You have served in a great interstellar navy of the Alliance, Empire or Federation. Working aboard a capital spacecraft such as a Farragut or Majestic battlecruiser, you have been part of a dedicated team of hundreds of personnel required to keep these enormous ships running. Such a career is excellent training for life in space, and there is little the galaxy can throw at you that you cannot overcome.'),\
    'offi':('Officer',1,[Effect('dip',10),Effect('intim',10),Effect('perc',10),Effect('tact',20)],'N/A','REQUIRES ARMY TRAINED OR NAVY TRAINED BACKGROUND','You are a formally trained officer in the military of one of the great powers of the galaxy (your previous background determines which service you are an officer in). As a military leader you are schooled in battle tactics, command and motivation. You might find it difficult to relinquish these traits now you are in civilian life.'),\
    'part':('Partner',1,[],'N/A',['patner'],'You do not travel space alone. You have a loyal companion who sticks by your side through thick and thin.'),\
    'pett':('Petty Criminal',1,[Effect('fight',10),Effect('kin_weap',10),Effect('parry',10),Effect('sleight',10),Effect('strwise',10)],'N/A','N/A','You were a small time crook, with a broad portfolio of mugging, theft and burglary to your name. It is impossible to get rich through such a life – the gang bosses make sure that no independent criminal ever gets too big for their boots, so after a few run-ins with the Don you decided to skip planets and find something more lucrative to do.'),\
    'pilo':('Pilot Trained',1,[Effect('ship_plt',20),Effect('ship_weap',20),Effect('sys',10)],'N/A','N/A','You have passed your flying licence for the operation of spacecraft, which includes the use of the generic systems, weapons and engine functions of conventional small spacecraft. Flying without a licence is a criminal offence but the number of unlicensed and uninsured pilots has risen sharply in the last few years.'),\
    'pit':('Pit Fighter ',1,[Effect('bluff',10),Effect('charm',20),Effect('fight',10),Effect('parry',10)],'N/A','N/A','You were a minor holovision celebrity, who fought in staged fights in filthy mud-filled pits. The show was supposed to be set on the rugged frontier world of New America in Quince, but was in fact filmed on Cubeo 3, on a comfortable set in the heart of the metropolis of Chengarn. The show followed your scripted life, your torrid love affairs, and even the occasional pit fight. Some ill-judged words to the studio producer saw your character written out, but you are still recognised by the less cultured members of Imperial society.'),\
    'police':('Police Officer',2,[Effect('cult_law',10),Effect('dip',10),Effect('dodge',10),Effect('eng_weap',20),Effect('fight',10),Effect('perc',20),Effect('ship_plt',10),Effect('ship_weap',10)],'N/A','N/A','You were or are a member of a system police or security service. You are extensively trained in detecting, tracking, and arresting criminals of all stripes and backgrounds. Modern police officers use spacecraft, ground vehicles, computers and a range of other technological devices to keep up with criminals, but a steady gun arm and a strong right hook remain crucial traits for a cop who wants to survive their beat.'),\
    'priv':('Private Detective',1,[Effect('eng_weap',10),Effect('insight',10),Effect('perc',10),Effect('sec',10),Effect('stealth',10)],'N/A','N/A','As long as people have kept secrets there have been those who specialise in uncovering them. The job of a private detective hasn’t changed much, suspicious partners made up the majority of your cases - but just sometimes something really juicy comes along. Uncovering corporate scandals, government incompetence and mob conspiracies are the real meat and drink to a detective.'),\
    'runa':('Ran Away From Home',1,[Effect('dodge',10),Effect('perc',10),Effect('sleight',10),Effect('strwise',10),Effect('surv',10)],'N/A','N/A','Home life has to be pretty awful to convince a child to run away. You missed out on a large chunk of your education, but gained some learning from the school of hard knocks. Life on the street was terrible, but has made you more self-reliant than most people in the galaxy. Presumably something happened to improve your life, but you’ll never forget those hard-learned skills as a member of the forgotten underclass.'),\
    'scie':('Scientist',1,[Effect('comp',10),Effect('sci',20)],'natural genius (science)','N/A','You are a highly intelligent theoretical scientist who has contributed to a number of fields in mathematics and physics. Being able to understand the nature of the universe, and unlocking the doors of ‘how’ and ‘why’ is your driven passion. Being a scientist will never make you rich, and perhaps too much time spent in the lab might close your mind to the infinite possibilities of the galaxy. No matter what you choose to do your ability to understand how the universe works will give you a big advantage.'),\
    'scout':('Scout Leader',1,[Effect('athlet',10),Effect('charm',10),Effect('kin_weap',10),Effect('nav',10),Effect('surv',10)],'N/A','N/A','Your homeworld was a luxurious green Earth-type planet. Too many people in the galaxy have never seen a real tree – not you. You revelled in play and sport in the great outdoors and were an enthusiastic young scout. In fact you found it quite hard to leave the organisation and stayed on as scout leader long after your peers grew up and derided you for your lack of ‘cool’. You don’t care. Where are they now? City brokers, factory workers? The wild is nurturing and honest, and will always call you home.'),\
    'snd':('Second Hand Spaceship Dealer',1,[Effect('bargin',20),Effect('plant_know',10),Effect('repair',10),Effect('trade',10)],'N/A','N/A','You are an expert at selling old, semi-functional spacecraft. You worked on a used spaceship lot in some dreary backwater space station, selling dreams to kids with no money and ‘fixer-uppers’ to fools who think they’ll get that old spaceship fixed just as soon as they’ve finished the bathroom. You didn’t get to keep the money you made, so you quit. Hell, if you’re going to rip people off you might as well get the money for it!'),\
    'secr':('Secret Agent',2,[Effect('bluff',10),Effect('charm',10),Effect('comp',10),Effect('dodge',10),Effect('eng_weap',10),Effect('insight',10),Effect('sec',20),Effect('stealth',20)],'N/A','N/A','You were an ‘information retrieval agent’ for a government or large corporation. Your job was to break into corporate headquarters and steal their secrets. Failing a mission generally meant death from the trigger-happy targets of your theft, so you must have been a success. Lying, stealing, charming and avoiding were your main talents. If you ever had to pull out a weapon chances are the mission would have been a failure.'),\
    'self':('Self-Taught',1,[Effect(Empty(),10), Effect(Empty(),10)],[Empty()],'Any two Skills +10','You are a highly disciplined person and have taught yourself the skills you need through sheer perseverance. You may not have as many Skills as other people, but you are much more focused.'),\
    'ship':('Ship Hand',1,[Effect('kin_weap',10),Effect('repair',10),Effect('ship_weap',10),Effect('sys',20)],'N/A','N/A','You’ve worked on large spaceships for a good portion of your life. You are excellent in a supporting role, able to operate turrets, scanner systems and even repair the ship with some skill.'),\
    'slvs':('Slave Soldier ',1,[Effect('bluff',10),Effect('charm',10),Effect('dodge',10),Effect('eng_weap',10),Effect('veh_weap',10)],'N/A','N/A','The tradition of slavery is an entrenched component of Imperial society.  Despite the nauseous feelings it provokes in other nations, slavery remains a publicly popular option for insolvent Imperial citizens.  Victims of legal cases, poor students, and rash entrepreneurs all benefit from a system that removes all debt and prevents them from being executed by the internal security force. Being a slave soldier for the Empire is actually a rather lucky placement.  Few people want to mess with the Imperial navy, so it is safer than it seems.  However you have to be quite wily; a slave gets the worst equipment, quarters, and rations of any serving soldier in the navy.'),\
    'smug':('Smuggler',1,[Effect('bargin',10),Effect('ship_plt',10),Effect('sys',10),Effect('tact',10),Effect('veh_plt',10)],'N/A','N/A','Smuggling is all about opportunity and timing.  Dealing in illegal goods is only worth it if the customers are desperate.  Sneaking illegal goods into a space port can only be done if the security services are busy scanning the wrong target.  If smuggling is your career, you need to be fast, decisive, and uninterested in the consequences of your actions. '),\
    'sport':('Sports College',1,[Effect('athlet',20),Effect('dodge',10)],['quick runner'],'N/A','You are extremely physically fit and have attended sports college. You never managed to advance into the professional leagues of your game but you are, nonetheless, at the peak of physical excellence, able to run, jump and swim faster than most of your colleagues.'),\
    'stock':('Stockbroker',1,[Effect('bluff',10),Effect('fight',10),Effect('intim',10),Effect('trade',20)],'N/A','N/A','You used to work for a major interstellar bank, such as the Bank of Zaonce or the Federal Cooperative. With artificial intelligence banned the stock markets are run by humans. This makes for a volatile and high stress environment, full of intimidation, blackmail and the occasional murder. It is a hard profession to leave … the addictive quality of earning outrageous money can cost a person their soul.'),\
    'teach':('Teacher',1,[Effect('cult_law',10),Effect('dip',10),Effect('intim',10),Effect('perc',10),Effect('sci',10)],'N/A','N/A','You bear the noble duty to educate the next generation of ungrateful brats. A good teacher can inspire their students to great heights. Bad teachers, like you, rely on brute force, intimidation and a loud voice to do more or less the same. Most teachers only last a couple of years in the job before undertaking less stressful work, like front line combat or bomb disposal.'),\
    'doc':('Trained Doctor',1,[Effect('cyber',20),Effect('med',20),Effect('sci',10)],'N/A','N/A','Getting a medical degree is probably the most significant achievement of your life. These days a doctor needs not only expertise in biology and chemistry, but also cybernetics. You haven’t finished your specialisation, but even without it a trained doctor can find work anywhere; especially in occupations that expose the team to high amounts of risk.'),\
    'treas':('Treasure Hunter',1,[Effect('fight',10),Effect('kin_weap',10),Effect('nav',10),Effect('plant_know',10),Effect('veh_plt',10)],'N/A','N/A','Some people explore the galaxy purely to increase their knowledge, or to behold the strange and wonderful sights of an infinite universe. Personally you would be happy if every planet you landed on looked the same, provided they were stuffed with rare minerals, crashed treasure ships or abandoned military outposts. You’re in it for the money, and you know the best places in the galaxy to go looking for it!'),\
    'truck':('Trucker',1,[Effect('trade',10),Effect('veh_plt',10),Effect('veh_weap',10)],['tough'],'N/A','Bulging biceps, the stink of stale sweat, grim halitosis… but enough about Cobra pilots. You’re a trucker, a rougher, tougher breed than any of those spaceship flying wimps! They should try driving across unpaved badlands in a suspension-free frontier truck, beset by every missile wielding bandit or punk in a dune buggy who’d like a taste of your sweet, sweet cargo. You’ll have to leave the wheel for a bit whilst you spend some time doing space trading, but you’ll be back. Just wait until those outlaws see you driving around in a brand new light tank! Then we’ll see who needs to run.'),\
    'uni':('University Graduate',1,[Effect(Empty(),20),Effect(Empty(),10),Effect(Empty(),10)],'N/A',"One Intelligence Skill +20 & Two Intelligence Skills +10",'Universities cost a fortune these days, so those lucky enough to be able to go can get a real leg up in life. Just being qualified to apply for university means you are already accomplished in physical and social science, your degree is really just the icing on the cake.'),\
    'vehi':('Vehicle Nut',1,[Effect('repair',10),Effect('veh_plt',20),Effect('veh_weap',20)],'N/A','N/A','From the first time you were strapped into a car as baby you fell in love with ground vehicles. The speed, the skidding, the traction; the entire physical and emotional experience of going fast close to the ground is exhilarating. You collected and tinkered with wheeled vehicles of all sorts, and enjoyed nothing more than a good destruction derby. No matter what your eventual occupation you have always tried to bring your love of vehicles with you, whether that’s as a racer, a tank driver or a scout. Vrroooomm!!!'),\
    'wage':('Wage Slave',1,[Effect('bargin',10),Effect('comp',10),Effect('cult_law',10),Effect('dip',10),Effect('sec',10)],'N/A','N/A','You have worked for one of the galaxy’s worst corporations in a badly paid administrative role. The company paid you just enough money to keep you alive, clean and housed, but without the ability to gather any savings or improve your lot.  You were bullied, oppressed and threatened as a matter of course. Toilet breaks were timed, your appearance and speech strictly regulated, and you were subjected to constant appraisal meetings at which your managers would browbeat you into sacrificing holiday and working overtime for no pay.  Leaving that behind wasn’t easy, but you have gained an exact knowledge of how corporations work and protect themselves. Could be handy if you ever wanted to pay them a little visit in the future…'),\
    'wise':('Wise Guy',2,[Effect('dodge',10),Effect('gambling',10),Effect('hvy_weap',10),Effect('kin_weap',10),Effect('med',10),Effect('mel_weap',10),Effect('strwise',20),Effect('tact',10),Effect('veh_weap',10)],'N/A','N/A','Every criminal organisation needs a fixer, someone who can cope with any situation the gang can get themselves into, whether it’s combat, disposing of dead bodies, or saving the life of a dying drug addict. The sheer versatility of the wise guy is a wonder to the common thug, who can only dream of receiving the same kind of respect.'),\
    'xeno':('Xenobiologist',1,[Effect('med',20),Effect('plant_know',10),Effect('sci',20)],'N/A','N/A','Humans have always needed other life-forms for survival, whether for medicine, or labour. That hasn’t stopped now humanity has exploded into the galaxy. Microbes need to be examined, alien animals studied and dissected.  New compounds can be found in infinite variety across the myriad of Earth-like worlds in the universe. As a trained Xenobiologist, you hunger for new specimens and deadly new bacteria to examine.  It’s an exciting time, and your research is just beginning!'),\
    }

KARMA_CAPABS = {'itf':('In There First ',3,True,True,True,False,'Gain a +5 bonus to your Initiative check.','N/A','N/A','Your weapon is out even as the pirate is reaching for his holster'),\
    'conc':('Concentration',3,False,False,False,True,'You can re-roll the failed Skill check.',' You have just failed a Skill check.','N/A','“Ten seconds until detonation,” intones the computer as you attempt to disarm the bomb. Focus! One wrong move and you’re done for!'),\
    'esca':('Escape Death',100,True,True,True,True,'You escape or avoid an attack that just killed you or reduced your Endurance to less than 1.','N/A','N/A','You emerge from the ashes of the burning tank, brushing the dust casually from your jacket as you do so.'),\
    'skil':('Skill Boost',2,False,False,False,True,'Gain a +2 bonus to your chosen Skill for this Skill check.','N/A','Non-Personal Combat or Vehicle Skill when you choose this Karmic Capability','The pressure is on. If you can’t get this airlock open in the next ten seconds the team will suffocate.'),\
    'pene':('Penetrating Shot',5,False,False,True,False,'When your opponent takes damage their armour absorption is ignored for this attack.','N/A','N/A','You peer through the sights of your rifle, lining up the weak chink of armour between the shoulder and joint…'),\
    'poin':('Point Blank Shot',3,False,False,True,False,' When making an attack at point blank range you don’t provoke a free attack.','N/A','N/A','Sighing wearily, you shoot the swordsman right in the face.'),\
    'blur':('Blur Of Steel',3,False,False,True,False,'You add a +2 bonus to the Melee attack you just made.','N/A','N/A','Your blade flashes and swipes before the enemy, before slicing in from an unexpected direction.'),\
    'crac':('Crack Shot',4,False,False,True,False,'In the midst of the firefight you find an inner moment of calm. Time seems to slow as you carefully aim your weapon at the enemy.','N/A','N/A','In the midst of the firefight you find an inner moment of calm. Time seems to slow as you carefully aim your weapon at the enemy.'),\
    'dive':('Dive Aside',5,False,False,True,False,'Gain a +5 bonus to your Defence (Dodge) against an attack that would hit you.','N/A','N/A','The house detonates behind you, and you hurl yourself through the air to escape the explosion.'),\
    'duck':('Duck!',2,False,False,True,False,'Gain a +2 bonus to your Defence (Dodge) against an attack that would hit you.','N/A','N/A','Your adrenaline pumping, you lurch aside as the energy beam sizzles across your flight suit.'),\
    'lead':('Eat Lead Sucker!',5,False,False,True,False,'If you hit your target with a Burst Weapon, inflict maximum Burst damage on them.','N/A','N/A','Your enemy’s body jerks and writhes, as every bullet from your autopistol impacts into their body.'),\
    'fire':('Fire In The Hold',3,False,False,True,False,'You can re-roll a scatter when missing with a grenade.','N/A','N/A','The smuggler looks down casually to see what just landed square at his feet. It’s the last thing  he ever sees.'),\
    'foll':('Follow Up',6,False,False,True,False,'Make another attack with the same weapon against the opponent immediately.','You have just scored a hit with a ranged weapon against an opponent.','N/A','The gangster’s body jolts as the rounds from your autopistol slam into him.  You don’t let up, keeping the trigger pulled until he sprawls to the floor…'),\
    'down':('Get Down!',3,False,False,True,False,'Choose an ally that you can see and who can hear you. They gain a +2 bonus to their Defence (Dodge or Parry) against an attack that just hit them.','N/A','N/A','“Baxter, behind you!” snaps Jenya, and you instinctively duck as the axe sails over your head.'),\
    'hard':('Hard Boiled',8,False,False,True,False,' Make two ranged weapon attacks, one with each gun in your hands, with no penalties for using two guns at the same time. Additionally your Defence (Dodge) is 10 until your next turn, regardless of your dodge Skill','You must be holding a one-handed energy or Kinetic weapon in each hand and are not knocked over.','N/A','It’s time to take these fools down. Pulling a spare gun from your coat you leap through the doorway, guns blazing, enemy fire whizzing past your head as you fly through the air…'),\
    'hunt':('Hunter',1,False,False,True,False,'When making an attack roll against an Alien Animal or Biomod, you can add your Survival Skill bonus to the roll as well as the relevant weapon Skill bonus.','N/A','N/A','The Narseer rears up before you … its last mistake.  Aiming straight for its jugular, you tear a bloody hole in the alien lizard’s skin.'),\
    'inco':('Incoming!',3,False,False,True,False,'If you are in the fatal radius of the explosive you move until you are in the injury radius. If you are in the injury radius you move until you are outside the radius. Those adjacent to you can do the same.','N/A','N/A','You have an allergy to high explosives and no one can run as fast as you when the shoulder-mounted missile launchers come out'),\
    'iron':('Iron Willed',3,False,False,True,False,'You are unaffected by any attack or condition that causes you to hallucinate, or lose control of your actions.','N/A','N/A','They’ve tried for days to make you crack. Drugs, water-boarding, bright lights … they’ll never break you!'),\
    'kiss':('Kiss, Kiss, Bang, Bang',4,False,False,True,False,'You automatically hit your target with a weapon you are carrying with the One-Handed trait. If the weapon inflicts Burst damage, you roll the maximum number of dice. If not, your weapon inflicts double damage.','You must be alone with your target, and have just completed a successful Charm Skill check.','N/A','“So,” you say, flashing a smile at the corrupt security guard. “What time do you get off?” The guard grins, gazing shamelessly at your body. “For you, honey, I can…” but he never finishes. There is a loud bang, and he jolts, a growing red stain spreading across his stomach. You tuck away your laser pistol as he slumps to the ground.'),\
    'last':('Last Minute Deflection',3,False,False,True,False,'Gain a +3 bonus to your Parry against an attack that would hit you.','N/A','N/A','You knock aside the cyborg’s wrist just as its terrible cyberclaws slash towards your face.'),\
    'quic':('Quick Loader',2,False,False,True,False,'You immediately reload the weapon. This does not use up your next turn’s action.','You have just used the last ammo point on a weapon you were firing and you have a spare clip.','N/A','As the last bullet spits from your assault rifle, you rip the clip out and replace it with fluidity and speed.'),\
    'ripo':('Riposte ',1,False,False,True,False,'You can counter attack your enemy’s counter attack.','N/A','N/A','Sword blades clash in a whirl of steel. You lunge, but miss, the cultist swinging round to exploit your mistake. With lighting reflexes you parry again, deflecting the Death Cultist’s own sword right into his throat.'),\
    'slam':('Slam',2,False,False,True,False,'The enemy is knocked over, regardless of the damage result.','You have just hit an opponent with a Melee or Fighting attack.','N/A','You ram your fist under the pirate’s jaw. He drops like a sack of potatoes.'),\
    'spin':('Spinning Kick',3,False,False,True,False,'Make a Fighting attack against the enemy who just attacked you. They do not get to add their Parry or Dodge bonus against this attack. You can then make a counterattack.','You have just parried and the enemy missed you.','N/A','You smoothly parry the attack, spinning round as you do so to plant your foot into your opponent’s neck!'),\
    'stay':('Stay Standing',1,False,False,True,False,'An attack that just hit you does not knock you down.','N/A','N/A','You stagger, but do not fall as the shotgun pellets crack into your breastplate.'),\
    'suck':('Sucker Punch',2,False,False,True,False,'Make another Fighting attack immediately, ignoring the enemy’s Dodge or Parry bonus.','You just made a Fighting attack, whether that attack hits or misses.','N/A','You craftily sneak another punch in when the enemy least expects it.'),\
    'weak':('Weak Point',3,False,False,True,False,'Have your opponent make a Hardened armour check (opponents wearing armour without the Hardened quality fail automatically). If they fail, their armour does not protect them against the damage from this attack.',' You have just hit your opponent with a ranged attack but have not yet rolled the Damage.','N/A','Your eye flicks to the gap between the walker drone’s plated armour.  With pinpoint precision, your shots blast straight into the hole.'),\
    'with':('Without Even Looking…',4,False,False,True,False,'Make a ranged attack against a different enemy who is behind you or to the side of you with your one-handed Energy or Kinetic weapon. You suffer no penalty To Hit.','You must have a one-handed energy or Kinetic weapon in your hand.  You have just attacked and hit an opponent in front of you.','N/A','Your laser pistol sizzles through the anarchist as his friend tries to sneak up behind you. Without turning you point your pistol behind you and fry the sneaky punk.'),\
    'dili':('Diligent Medic',3,False,False,False,True,'You can use a Medpack on someone again, even if they’re already been treated within the last six hours.','N/A','N/A','You have to get your friend back on their feet. You redress their bandages and give them an extra shot of stimulants.'),\
    'dril':('Drill Sergeant',1,False,False,False,True,'You can double your Skill bonus when making a Social skill check to influence military personnel.','N/A','N/A','Soldiers respect you. Or are frightened by your loud voice. Either is fine.'),\
    'ever':('Everybody Pipe Down',4,False,False,False,True,'You and allies gain +2 bonus to Stealth Checks.','N/A','N/A','You peek around the corner to see a platoon of heavily armed corporate soldiers. You raise your hand to your crouching comrades to silence them.'),\
    'ghos':('Ghost',4,False,False,False,True,'You gain a +4 bonus to Stealth Checks when following someone.','N/A','N/A','You vanish into the crowd, keeping a close eye on the enemy spy as she anxiously looks around herself. '),\
    'hone':('Honey Trap',4,False,False,False,True,'Rather than charm someone you can attempt to seduce them. Provided you are sexually compatible make a Charm Skill Check against the target’s Insight Skill Check. If you are successful the target becomes much more gullible and foolish in your presence, and cannot add their Insight Bonus when you make any further Charm, Bargain or Diplomacy checks against them.','You must be in a non-hostile situation to use this Skill.','N/A','You saunter by your mark, just close enough so your perfume can waft by his nose. He turns, looks and is smitten in a second.'),\
    'liar':('Liar, Liar!',2,False,False,False,True,'If you are making an Insight check to determine if someone is lying to you, gain a +4 bonus','N/A','N/A','“Don’t tell me you weren’t there, Henning!” you snap at the sweating prisoner. “The truth is plastered all over your face!”'),\
    'resu':('Resuscitate',8,False,False,False,True,'If a party member has been killed within the last minute, make a Difficulty 13 Medicine check. On a success they do not die, but remain unconscious for twenty four hours with 0 Endurance points. You can attempt this multiple times provided you have enough Karma.','N/A','N/A','“Don’t give up on me, Foster!” you cry, pressing on his bleeding chest to try and restart his heart.'),\
    'secr':('Secret Markets',2,False,False,False,True,'You can re-roll a result you or the GM just made on the Advanced Trading tables, and then choose which result applies.','N/A','N/A','You barely glance at the commodity market board. That’s not where the real deals are made…'),\
    '3dth':('3D Thinking',2,True,False,False,False,'Use when you have just completed the Flight Assist Off action. You can keep your spaceship’s Agility score when calculating your defence.','N/A','N/A','Newtonian physics don’t faze you. You can spin and jink your ship just as well with Flight Assist Off.'),\
    'burn':('Burnout',3,True,False,False,False,'This attack becomes a critical hit, provided it has damaged the hull of the enemy spaceship.','N/A','N/A','You grit your teeth as your multi-cannons rip across the enemy hull, tearing into its thrusters.'),\
    'dont':('Don’t Give Out On Me Yet!',5,True,False,False,False,'The component is instead reduced to 5 Strength points and still functions.','A component has just been reduced to 0 Strength by a critical hit.','N/A','Your thrusters are hanging by a thread … but they’re okay!'),\
    'ihav':('I Have You Now…',3,True,False,False,False,'Gain +2 bonus to your current Dogfighting check.','N/A','N/A','The enemy Eagle twists and turns but cannot escape your sights. You stick close to the enemy’s tail and open fire.'),\
    'jink':('Jink',2,True,False,False,False,'Gain a +2 bonus to your Spaceship Defence against an attack that would hit you.','N/A','N/A','You never keep your ship flying in a straight line, your lateral thrusters flaming as you bob and weave through space.'),\
    'miss':('Karmic Missile',3,True,False,False,False,'ECM (Electronic Counter Measures) and Point Defence Counter Measures have no effect against this missile attack.','N/A','N/A','Perhaps the enemy’s countermeasures didn’t engage. Perhaps the missile’s targeting systems are faulty. Either way this missile seems to blithely ignore the countermeasures used against it.'),\
    'line':('Line Em Up!',3,True,False,False,False,'When firing broadsides in spaceship combat you can keep firing at the same target even if you miss with a turret.','N/A','N/A','You roll your Anaconda on its axis, allowing your turrets to blast the harassing Vulture one by one.'),\
    'rapi':('Rapid Deployment',3,True,False,False,False,'You can use this Karma Capability yourself, if you are flying the fighter, or grant it to a ship that has just launched from your hangar. The ship-launched fighter immediately takes its turn. Once this free turn is performed, roll Initiative as normal for the fighter, and then resume the mothership’s turn.','N/A','N/A','Your ship-launched fighter soars out of the mothership, guns blazing even as it swoops from the hangar'),\
    'spin':('Spin Wildly',5,True,False,False,False,'Gain a +5 bonus to your Spaceship Defence against an attack that would hit you.','N/A','N/A','Laser bolts scream past you harmlessly as you spin your ship through the firestorm.'),\
    'wors':('Worse Than It Looks',3,True,False,False,False,'When targeting a ship’s components, do not suffer any penalties To Hit.','N/A','N/A','Don’t worry, kid, they’ll never hit the power plant from here … oh…'),\
    'gmoh':('Get Me Outta Here!',3,True,True,False,False,'Gain a +4 bonus to your Pursuit check when disengaging.','N/A','N/A','You activate thrusters, dive and then pull up sharply, desperately hoping this will shake the Eagle off your tail.'),\
    'inst':('Instinctive Aim',4,True,True,False,False,'You add a +2 bonus to the Spaceship or Vehicle attack you just made.','N/A','N/A','You pull the trigger even before the enemy obligingly flies into your sights.'),\
    'avoi':('Avoid Lock',3,False,True,False,False,'Missiles can’t target your vehicle til your next turn.','N/A','N/A','Hearing the tell-tale bleep of a missile lock you swerve your SRV violently left and right to confuse the enemy’s targeting systems.'),\
    'brea':('Break Right!',2,False,True,False,False,'Gain a +2 bonus to your Vehicle Defence against an attack that would hit you.','N/A','N/A','Your eyes flash as you spot the enemy turret hone in on your SRV. At the last moment you turn sharply to the right to throw off their aim.'),\
    'gsgr':('Get Some Grip',2,False,True,False,False,'Gain a +5 bonus to your Vehicle Piloting check to avoid Obstacles','N/A','N/A','Wrestling with the steering wheel you manage to keep the cargo truck under control as you slam on the breaks.'),\
    'hand':('Handbrake Turn',5,False,True,False,False,'Gain a +5 bonus to your Vehicle Defence against an attack that would hit you.','N/A','N/A','It might invalidate the warranty on your SRV, but you wrench the handbrake and skid sharply aside as the cannon shot thuds into the ground ahead of you.'),\
    'powe':('Power Bounce',5,False,True,False,False,'If you start up-close in vehicle combat and are moving at Speed 3 or more, you can use your action to activate your thrusters to bound away from combat. Fire your turret, if you have one, at any target up-close and then move yourself to atdistance. (Enemies cannot pursue you.)','N/A','N/A','You just can’t shake that enemy track-biker. Activating your thrusters just as you crest a hill you soar into the air, spinning your light-tank around to blast at the enemy.'),\
    'swip':('Swipe',4,False,True,False,False,'Instead of firing your weapons you Ram an opponent in such a way as to minimise your own damage and maximise theirs. Make a Ram attack, with a +2 bonus To Hit. If you hit you take half normal damage and do not go out of control. Your enemy takes full damage and must make two obstacle checks in their next turn.','N/A','N/A','You smash your SRV across the side of the truck, grinning as the truck careers off the road into a ditch.'),\
    'terr':('Terrain Breaking',1,False,True,False,False,' Unless the terrain you are driving on is perfectly flat (a road, an ice sheet, etc.) you can accelerate or decelerate 1 point extra.','N/A','N/A','You like to use the terrain to alter the speed of your vehicle, riding up hills to slow down, or down slopes to accelerate.'),\
    }