import os, random, pygame, numpy
class Weapon:
	def __init__(self, name, description, cost, meleemindam, meleemaxdam, critmult, critchance, psuc, ppsuc, pfail, pcfail, shield, dex, mgcwhitebonus, mgcblackbonus, mgcgreenbonus, mgcgraybonus):
		#name, string discription of weapon, minimum damage, maximum damage, crit %(as decimal, and so will all the others after it be) chance, parry crit % chance, parry success % chance, partial parry success chance, parry fail chance, parry critical fail chance
		self.type = "Weapon"
		self.NAME = name
		self.description = description
		self.cost = cost
		self.mindam = meleemindam
		self.maxdam = meleemaxdam
		self.crmult = critmult
		self.crit = critchance
		self.psuc = psuc
		self.prtpsuc = ppsuc
		self.pfail = pfail
		self.pcrfail = pcfail
		self.shield = shield
		self.DEX = dex
		self.wbonus = mgcwhitebonus
		self.bbonus = mgcblackbonus
		self.grnbonus = mgcgreenbonus
		self.grybonus = mgcgraybonus

class MagicBook(Weapon):
    def __init__(self, name, description, cost, mgcwhitebonus, mgcblackbonus, mgcgreenbonus, mgcgraybonus):
        super().__init__(name, description, cost, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, mgcwhitebonus, mgcblackbonus, mgcgreenbonus, mgcgraybonus)
        self.type = "Magic Book"

		
#swords
iron_sword = Weapon("Iron Sword", "A simple and slightly rusty sword made of iron", 0, 3, 6, 2, 0.05, 0.15, 0.2, 0.55, 0.05, 0, 1, 0, 0, 0, 0)


#daggers
iron_dagger = Weapon("Iron Dagger", "A simple and slightly rusty dagger made of iron", 0, 1, 4, 4, 0.2, 0.3, 0.2, 0.55, 0.05, 0, 2, 0, 0, 0, 0)


#warhammers
iron_warhammer = Weapon("Iron Warhammer", "A simple and slightly rusty sword made of iron", 0, 5, 8, 1, 0, 0.4, 0.0, 0.55, 0.05, 0, -1, 0, 0, 0, 0)


#shields
iron_shield = Weapon("Iron Shield", "A simple and slightly rusty sword made of iron", 0, 5, 8, 1, 0.1, 0.2, 0.3, 0.4, 0, 3, 0, 0, 0, 0, 0)

#magic
tatered_spellbook = Weapon("Spellbook", "a old and simplistic spellbook battered and worn", 0, 1, 3, 2, 0.05, 0.1, 0.15, 0.6, 0.05, 0, 0, 1, 1, 1, 1)

#bows
small_shortbow = Weapon("Simple Shortbow", "A worn out and small shortbow", 0, 2, 5, 2.5, 0.05, 0.1, 0.1, 0.65, 0.1, 0, 2, 0, 0, 2, 0)

# One-handed swords
Short_Sword = Weapon("Short Sword", "A simple but effective sword.", 10, 4, 1, "Sword", 1, 0, 0, 0, 0, 0, 0, 0, 0)
Scimitar = Weapon("Scimitar", "A curved sword that can slash through flesh and bone with ease.", 20, 6, 2, "Sword", 2, 0, 0, 0, 0, 0, 0, 0, 0)
Rapier = Weapon("Rapier", "A thin, pointed sword that can pierce through armor.", 30, 8, 3, "Sword", 0, 1, 0, 0, 0, 0, 0, 0, 0)

# Two-handed swords
Great_Sword = Weapon("Great Sword", "A massive sword that requires great strength to wield effectively.", 50, 12, 4, "Sword", 3, 0, 0, 0, 0, 0, 0, 0, 0)
Claymore = Weapon("Claymore", "A two-handed sword with a wide blade that can cleave through multiple enemies at once.", 80, 16, 5, "Sword", 5, 0, 0, 0, 0, 0, 0, 0, 0)
Bastard_Sword = Weapon("Bastard Sword", "A versatile sword that can be used with one or two hands.", 100, 20, 6, "Sword", 2, 2, 0, 0, 0, 0, 0, 0, 0)

# Axes
Hand_Axe = Weapon("Hand Axe", "A small axe that can be wielded with one hand.", 15, 6, 2, "Axe", 2, 0, 0, 0, 0, 0, 0, 0, 0)
Battle_Axe = Weapon("Battle Axe", "A heavy axe that can deal massive damage but is slow to swing.", 35, 10, 4, "Axe", 4, 0, 0, 0, 0, 0, 0, 0, 0)
Greataxe = Weapon("Greataxe", "A massive two-handed axe that can cleave through enemies with ease.", 60, 15, 6, "Axe", 5, 0, 0, 0, 0, 0, 0, 0, 0)

# Spears
Short_Spear = Weapon("Short Spear", "A basic spear that can be used both for stabbing and throwing.", 10, 4, 1, "Spear", 1, 0, 0, 0, 0, 0, 0, 0, 0)
Halberd = Weapon("Halberd", "A polearm with a blade on one end and a spike on the other, allowing for both stabbing and slashing attacks.", 40, 12, 4, "Spear", 4, 0, 0, 0, 0, 0, 0, 0, 0)
Glaive = Weapon("Glaive", "A long polearm with a curved blade at the end




#secret weapons
gob_mace_shield = Weapon("Mace of The Dying Goblns", "A mace directly forged by the final standing goblins sacrificing themself into a lava furnace to create the very powerful metal of the mace out of their scales and bones, giving this weapon magical properties and its wielder a fierce side boss like power.", 0, 6, 8, 2, 0.1, 0.25, 0.1, 0.5, 0, 2, 0, 2, 1, 3, 1)

#all weapons the player chooses from at the begining are listed below
starter_weapon_list = [iron_sword, iron_dagger, iron_warhammer, iron_shield, tatered_spellbook, small_shortbow]
all_weapon_list = [iron_sword, iron_dagger, iron_warhammer, iron_shield, tatered_spellbook, small_shortbow, gob_mace_shield]


#NO WEAPON
NOWEAPON = Weapon("ERROR", "NO WEAPON ERROR, IF YOU HAVE THIS THERE IS AN ERROR", 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0)