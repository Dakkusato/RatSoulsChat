import os, numpy, pygame, time

#setup class for armor
class Armor():
	def __init__(self, name, description, cost, defense, evasion, fire_res, ice_res, air_res, earth_res, poison_res, mgcwhitebonus, mgcblackbonus, mgcgreenbonus, mgcgraybonus):
		self.type = "armor"
		self.NAME = name
		self.DESC = description
		self.COST = cost
		self.DEF = defense
		self.EVA = evasion
		self.FRES = fire_res
		self.IRES = ice_res
		self.ARES = air_res
		self.ERES = earth_res
		self.PRES = poison_res
		self.wbonus = mgcwhitebonus
		self.bbonus = mgcblackbonus
		self.grnbonus = mgcgreenbonus
		self.grybonus = mgcgraybonus


#plate armor
Iron_Splint = Armor("Iron Splint Armor", "Armor made with many strips of metal covering the torso", 0, 3, 1, False, False, False, False, False, 0, 0, 0, 0)

#leather armor
Padded_Cloth = Armor("Padded Cloth Armor", "Barely even armor, made from cloths piled on one another to form a protective and unrestrictive padding.", 0, 1, 2, False, False, True, True, False, 0, 0, 0, 0)

#robes
Novice_Robes = Armor("Novice Robes", "Robes, pretty much no protection at all but it does provide a boost to your magic", 0, 0, 1, False, False, False, False, False, 2, 2, 2, 2)

starter_armor_list = [Iron_Splint, Padded_Cloth, Novice_Robes]
all_armor_list = [Iron_Splint, Padded_Cloth, Novice_Robes]



#NO ARMOR
NOARMOR = Armor("ERROR", "NO WEAPON, IF YOU SEE OR HAVE THIS THERE IS AN ERROR", 0, 0, 0, False, False, False, False, False, 0, 0, 0, 0)
