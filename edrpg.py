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
        self.pack= []
        self.ship_inv= []
        self.cash = Money(1000,0,0)
        
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
        


        

        





# Constants 
RANKS = [Rank("Harmless",0,40,10,3,20), Rank("Mostly Harmless", 8, 50, 11, 4, 25),\
    Rank("Novice", 20, 55, 12, 5, 30), Rank("Competent", 40, 60, 13, 6, 35),\
    Rank("Expert", 70, 65, 14, 7, 40), Rank("Master", 100, 70, 15, 8, 45),\
    Rank("Dangerous", 150, 80, 16, 9, 50), Rank("Deadly", 200, 90, 17, 10, 55),\
    Rank("Elite", 300, 100, 18, 11, 60)]
