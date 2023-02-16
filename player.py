import random, os, time, equipment.weapons, equipment.armor
PROTAGNAME = "BLANK"
class CharacterStats():
	def __init__(self, NAME, XP, HP, MHP, DEF, EVA, STR, ARC, HL, EquipedWeapon, EquipedArmor):
#INFO
		self.NAME = NAME #Character Name
		self.TOTALXP = XP #Total XP over career

#EQUIPMENT
		self.WEP = EquipedWeapon
		self.ARM = EquipedArmor
		
#STATS
		self.HP = HP #current HP
		self.MHP = MHP #max HP
		self.EXP = XP #Ammount of non-spent XP
		self.minatk = self.WEP.mindam+STR #Min attack damage
		self.maxatk = self.WEP.maxdam+STR #max attack damage
		self.HoldLevel = HL #How much have they held the line
		self.STR = STR #modifies melee damage
		self.ARC = ARC #modifies ARCane talent
		self.DEF = self.ARM.DEF+self.WEP.shield
		self.EVA = self.ARM.EVA+self.WEP.DEX
#MAGIC MODIFIERS
		self.FRES = self.ARM.FRES
		self.IRES = self.ARM.IRES
		self.ARES = self.ARM.ARES
		self.ERES = self.ARM.ERES
		self.PRES = self.ARM.PRES
		self.wbonus = ARC+self.WEP.wbonus+self.ARM.wbonus
		self.bbonus = ARC+self.WEP.bbonus+self.ARM.bbonus
		self.grnbonus = ARC+self.WEP.grnbonus+self.ARM.grnbonus
		self.grybonus = ARC+self.WEP.grybonus+self.ARM.grybonus

#ELEMENTAL EFFECTS
		#Fire/burnt does a lot of damage for a short time, ice/frozen reduces damage, earth/stuck increases damage taken, poison does little damage for a long time, and lightening does a set ammount of damage in a single turn.
		self.BRT = 0 #time burnt
		self.BRTAMT = 0 #damage over time it does
		self.FRZ = 0 #time frozen
		self.FRZAMT = 0 #Damage reduced by freeze
		self.STK = 0 #Time stuck
		self.STKAMT = 0 #Ammount of damage taken MULTIPLIER
		self.PSN = 0 #time poisened
		self.PSNAMT = 0 #Ammount of damage taken by poison
		self.LGT = 0 #Time electrocuted
		self.LGTAMT = 0 #Ammount of damage taken by lightening
		







MainPlayer = CharacterStats("None", 0, 0, 0, 0, 0, 0, 0, 0, equipment.weapons.NOWEAPON, equipment.armor.NOARMOR)


GP = 0
XP = 0
#MPHP = 125  + (1.5*XP)
#PHP = 125 + (1.5*XP) #this is the HP of the player, I add 10 per 2 Kill_Count
#PHP = max(0, min(PHP, MPHP)) #attempting to set up a max HP system, failing, WIP
#to_hit = int((random.randint(1, 20))+(1*(XP/9)))
#patk = int(random.randint(3, 6)+((.02*XP))) #new player damage, it has a random ammount #replaced with weapon  damage instead

#patk = int(5+(.025*XP)) #this is the atk damage of the player, 0 will by default equal 1 damage and I will add 1 per lebel
"""
peva:
#player evasion chances, 5/20 default
will do this later, tight on time
"""

class InventoryClass():
    def __init__(self):
        self.items = []
        self.capacity = 20
        
    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item.NAME} added to inventory.")
        else:
            print("Inventory is full.")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.NAME} removed from inventory.")
        else:
            print(f"{item.NAME} is not in inventory.")
    
    def show_inventory(self):
        if self.items:
            print("Inventory:")
            for item in self.items:
                print(f"{item.NAME}")
        else:
            print("Inventory is empty.")



PlayerInventory = InventoryClass()