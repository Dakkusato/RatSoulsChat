import Death_Messeges
import random
import Death_Messeges2
#EnnAmt = random.randint(1, 4)
EnnAmt = 1
f0enn1 = random.randint(0,4)
f0enn2 = random.randint(0,4)
f0enn3 = random.randint(0,4)
f0enn4 = random.randint(0,4)
f1_roll = random.randint(0, 8)

class EnemyRat():
	def __init__(self, NAME, HP, MHP, MINATK, MAXATK, ARM, EVA, DeMe, FIRE_RES, ICE_RES, AIR_RES, EARTH_RES, POISON_RES, FIRE_WEAK, ICE_WEAK, AIR_WEAK, EARTH_WEAK, POISON_WEAK, MINGP, MAXGP, XPR):
		self.NAME = NAME
		self.HP = HP
		self.MHP = MHP
		self.MINATK = MINATK
		self.MAXATK = MAXATK
		self.ARM = ARM
		self.EVA = EVA
		self.DeMe = DeMe
		self.MINGP = MINGP
		self.MAXGP = MAXGP
		self.XP = XPR
		self.BLIND = 0 #blind duration

#ELEMENTS
		#Fire/burnt does a lot of damage for a short time, ice/frozen reduces damage, earth/stuck increases damage taken, poison does little damage for a long time, and lightening does a set ammount of damage in a single turn.
		self.BRT = 0 #time burnt
		self.BRTAMT = 0 #damage over time it does
		self.FRZ = 0 #time frozen
		self.FRZAMT = 0 #Damage reduced by freeze
		self.STK = 0 #Time stuck
		self.STKAMT = 0 #Ammount of damage taken MULTIPLIER
		self.PSN = 0 #time poisened
		self.PSNAMT = 0 #Ammount of damage taken by poison
		

if (f0enn1 == 0):
	enn1 = EnemyRat("Rat", 2, 2, 2, 3, 1, 2, Death_Messeges.RatDM, False, False, False, False, False, True, False, False, False, True, 1, 3, 5)
elif (f0enn1 == 1):
	enn1 = EnemyRat("Zombie Rat", 2, 2, 1, 3, 2, 1, Death_Messeges.ZRatDM, False, False, False, False, True, True, False, False, True, False, 2, 5, 7)
elif (f0enn1 == 2):
	enn1 = EnemyRat("Large Rat", 4, 4, 3, 5, 3, 1, Death_Messeges.LRatDM, False, False, True, False, True, True, False, False, False, False, 3, 5, 10)
elif (f0enn1 == 3):
	enn1 = EnemyRat("Golden Rat", 5, 5, 4, 6, 2, 1, Death_Messeges.GRatDM, True, False, False, True, True, False, True, False, False, False, 5, 8, 10)
elif (f0enn1 == 4):
	enn1 = EnemyRat("Gold Rat", 1, 1, 1, 2, 0, 0, Death_Messeges.GratDM, False, False, False, False, False, False, False, False, False, False, 15, 15, 1)



"""
#floor 1
if (f1_roll == 0):
	enn1 = "Samuri Rat"
	f1hp = 5
	f1atk = 7
	DeMe = Death_Messeges2.SamDM2
elif (f1_roll == 1):
	enn1 = "Zombie Rat"
	f1hp = 2
	f1atk = random.randint(1, 3)
	DeMe = Death_Messeges2.ZRatDM2
elif (f1_roll == 2):
	enn1 = "Knight Rat"
	f1hp = 8
	f1atk = 4
	DeMe = Death_Messeges2.KnDM2
elif (f1_roll == 3):
 enn1 = "Golden Rat"
 f1hp = 5
 f1atk = 6
 DeMe = Death_Messeges2.GRatDM2
elif (f1_roll == 4):
	enn1 = "Gold Rat"
	f1hp = 1
	f1atk = 0
	DeMe = Death_Messeges2.GratDM2
elif (f1_roll == 5):
	enn1 = "mouse"
	f1hp = 5
	f1atk = 2
	DeMe = Death_Messeges2.MoDm2
elif (f1_roll == 6):
	enn1 = "Mouse"
	f1hp = 8
	f1atk = 3
	DeMe = Death_Messeges2.MMoDm2
elif (f1_roll == 7):
	enn1 = "Guard Rat"
	f1hp = 5
	f1atk = 5
	DeMe = Death_Messeges2.SoldDM2
elif (f1_roll == 8):
	enn1 = "Ghost Rat"
	f1hp = 7
	f1atk = 2
	DeMe = Death_Messeges2.GhoDM2
 """