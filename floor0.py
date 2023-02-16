#imports
import os, random, time, pygame, json, equipment.weapons, equipment.armor, saves.SaveAndLoad, PlayerData
from player import GP
from player import MainPlayer

Gob_Mace_Found = False
Gob_Mace_Taken = False
savedata = False
data_loaded = False
PartyList = [MainPlayer]
#saved data stuff
if (data_loaded == True):
	pass
	#in the future here we will set variables to what they are in the loaded library
else:
	pass

#pygame variables

#variables
start = "no"
Kill_Count = 0  #new Kill_Count every kill
floor = 0  #the floor num goes up every 5 levels
DeMe = "Death Messege, if you see this, there is an error"
enn0 = "if you're seeing this, there is an error"
enemy_blind = "F"
sdmg = False
pdam = 0  #The amount of damage the player dealt this turn
rdam = 0  #The amount of damage the rat did to the
atk_select = True

#Player Save Data setup
PlayerData.SaveData = {
 "MPNAME": MainPlayer.NAME,
 "MPTXP": MainPlayer.TOTALXP,
 "MPHP": MainPlayer.HP,
 "MPMHP": MainPlayer.MHP,
 "MPEXP": MainPlayer.EXP,
 "MPWeapon": MainPlayer.WEP.NAME,
 "MPArmor": MainPlayer.ARM.NAME,
 "MPSTR": MainPlayer.STR,
 "MPARC": MainPlayer.ARC,
 "FRES": MainPlayer.FRES,
 "IRES": MainPlayer.IRES,
 "ARES": MainPlayer.ARES,
 "ERES": MainPlayer.ERES,
 "PRES": MainPlayer.PRES,
 "gold": GP,
 "KC": Kill_Count
}


#check weapon
def WepCheck():
	global PlayerData, MainPlayer
	for weapon in range(len(equipment.weapons.all_weapon_list)):
		WepName = str(PlayerData.SaveData["MPWeapon"])
		if WepName == equipment.weapons.all_weapon_list[weapon].NAME:
			MainPlayer.WEP = equipment.weapons.all_weapon_list[weapon]
		else:
			pass


def ArmCheck():
	global PlayerData, MainPlayer
	for armor in range(len(equipment.armor.all_armor_list)):
		WepName = PlayerData.SaveData["MPWeapon"]
		if WepName == equipment.armor.all_armor_list[armor].NAME:
			MainPlayer.ARM = equipment.armor.all_armor_list[armor]


#ELEMENT CHECKING
def apply_element_effects(enemies):
    for enemy in enemies:
        if enemy.BRT > 0:
            enemy.HP -= enemy.BRTAMT
            enemy.BRT -= 1
        if enemy.FRZ > 0:
            enemy.MAXATK = max(0, enemy.MAXATK - enemy.FRZAMT)
            enemy.FRZ -= 1
        if enemy.STK > 0:
            enemy.MAXATK *= enemy.STKAMT
            enemy.STK -= 1
        if enemy.PSN > 0:
            enemy.HP -= enemy.PSNAMT
            enemy.PSN -= 1


#UI stats
def PrintStats(user):
	print(
	 f"GP:{GP} Hold Level {user.HoldLevel}\n {user.NAME} xp:{user.TOTALXP} HP:{MainPlayer.HP} atk:{MINPATK}-{MAXPATK}\n {enn1.NAME}:{enn1.HP} atk:{MINEATK}-{MAXEATK}\n"
	)


time.sleep(0.0001)


#Attack functions
def BasicAtk(user):
	global Kill_Count, pdam, floor, Kill_Count, MainPlayer, to_hit
	if (to_hit == (21 - (20 * user.WEP.crit))):
		pdam += int(user.WEP.crmult * patk + MainPlayer.STR)
	elif (to_hit >= enn1.ARM):
		pdam += int(patk + MainPlayer.STR)
		#animation = basic_attack_hit
	else:
		pdam += 0
		#animation = basic_attack_miss


def Parry(user):
	global pdam, rdam
	parry_crit_success = 21 - (20 * user.WEP.crit)
	parry_success = parry_crit_success - (20 * user.WEP.psuc)
	parry_part_success = parry_success - (20 * user.WEP.prtpsuc)
	parry_fail = parry_part_success - (20 * user.WEP.pfail)
	parry_crit_fail = parry_fail - (20 * user.WEP.pcrfail)

	parc = random.randint(1, 20)
	#animation = parry_fail

	if (parc >= (parry_crit_success)):
		rdam = 0
		pdam += int(user.WEP.crmult * patk)
		#animation = parry_success

	elif (parc >= (parry_success)):
		rdam += 0
		pdam += int((.75 * user.WEP.crmult) * patk)
		#animation = parry_success

	elif (parc >= (parry_part_success)):
		rdam += 0
		pdam += int(patk)
		#animation = parry_success

	elif (parc >= parry_fail):
		rdam *= 2
		pdam += int(0)

	elif (parc >= parry_crit_fail):
		rdam *= 2
		pdam += int(0)

	else:
		os.system('clear')
		print(
		 "error: floor0, parry_critical_fail, weapon:", user.WEP,
		 "please screenshot and save the screenshot, restart the game, and if this persists sent the screenshot to RatSouls@gmail.com asking for help"
		)
		time.sleep(99999999999999)


def Blind():
	global enemy_blind, sdmg
	enemy_blind = "T1"
	sdmg = True
	if (Kill_Count == 8):
		print("YOU DISCOVERED ABILITY: BLIND")


def MgcHealing(user):
	global pdam, floor, Kill_Count, PHP, MPHP, HEAL
	if ((user.wbonus) >= (user.grybonus)):
		HEAL = int((random.randint(8, 15) + floor + (Kill_Count / 2)) +
		           (user.wbonus))
	if ((user.grybonus) < (user.wbonus)):
		HEAL = int((random.randint(8, 15) + floor + (Kill_Count / 2)) +
		           (user.grybonus))
	PHP += HEAL
	PHP = max(0, min(PHP, MPHP))
	#animation = heal


def MgcBolt(user, target):
	global Kill_Count, pdam, floor, Kill_Count, to_hit, MainPlayer, enn1
	if (to_hit >= enn1.ARM):
		if ((user.bbonus) >= (user.grybonus)):
			pdam += int(random.randint(3, 5) + (Kill_Count * 0.002) + (user.bbonus))
		if ((user.bbonus) < (user.grybonus)):
			pdam += int(random.randint(3, 5) + (Kill_Count * 0.002) + (user.grybonus))
	else:
		pdam += int(0)


def MgcEmber(user, target):
	global pdam, floor, Kill_Count, PHP, MPHP
	if ((user.bbonus) >= (user.grybonus) and (user.bbonus) >= user.grnbonus):
		pdam += int(random.randint(2, 3) + (Kill_Count * 0.002) + (user.bbonus))
		target.BRT += int(3 + (user.bbonus / 10))
	if ((user.grybonus) > ((user.bbonus)) and (user.grybonus) > (user.grnbonus)):
		pdam += int(random.randint(2, 3) + (Kill_Count * 0.002) + (user.grybonus))
		target.BRT += int(3 + (user.grybonus / 10))
	if ((user.grnbonus) > (user.bbonus) and (user.grnbonus) > (user.grybonus)):
		pdam += int(random.randint(2, 3) + (Kill_Count * 0.002) + (user.grnbonus))
		target.BRT += int(3 + (user.grnbonus / 10))


def MgcGlacialBlast(user, target):
	global pdam, floor, Kill_Count, PHP, MPHP
	if ((user.bbonus) >= (user.grybonus)):
		pdam = int(2 + (Kill_Count * 0.005) + (user.bbonus))
		target.FRZ += int(3 + (user.bbonus / 10))
	if ((user.bbonus) < (user.grybonus)):
		pdam = int(2 + (Kill_Count * 0.005) + (user.grybonus))
		target.FRZ += int(3 + (user.grybonus / 10))
		target.FRZAMT += int(3 + (user.grybonus / 10))


def Hold(user):
	global move, HoldLevel, rdam
	if user.HoldLevel < 5 and user.HoldLevel > -4:
		user.HoldLevel += 1
		if (user.DEF > user.EVA):
			rdam -= user.DEF
		else:
			rdam -= user.EVA
	else:
		move = "False"


def Burst(user):
	global HoldLevel, Kill_Count, pdam, patk, MainPlayer, enn1
	BrstAmt = int(
	 input(
	  "How many times would you like to burst? numbers only or this will crash"))
	if (user.HoldLevel - BrstAmt < -5):
		BrstAmt -= (-5) - (user.HoldLevel - BrstAmt)
	for x in range(BrstAmt):
		user.HoldLevel -= 1
		to_hit = int(random.randint(1, 20))
		if (to_hit == (21 - (20 * user.WEP.crit))):
			pdam += int(user.WEP.crmult * patk + MainPlayer.STR)
		elif (to_hit >= enn1.ARM and to_hit >= enn1.EVA):
			pdam += int(patk + MainPlayer.STR)
			#animation = basic_attack_hit
		else:
			pdam += 0
			#animation = basic_attack_miss


#ACTUAL GAME

#before the player has killed 9 enemies
while (MainPlayer.TOTALXP <= 500):
	#if player dies preform bellow
	if (MainPlayer.HP <= 0):
		os.system('clear')
		print("G A M E   O V E R \n you died to", enn0, "\n", enn1.DeMe)
	os.system('clear')  #put here so line 27 doesn't colapse bellow comments

	#floor one (total of 10)

	#HERE, I put the code for selecting enemy rats in RatClasses.py
	#from RatClasses import enn0, hp, atk, arm, DeMe, gpr
	from RatClasses import EnnAmt, enn1
	EnemyList = [enn1]
	while len(EnemyList) > EnnAmt:
		EnemyList.pop()


	PlayerList = [MainPlayer]

	#we reset the options
	move = "Error floor0, reset move error"
	atk_option = "Error floor0, reset atk_option error"
	mgc_option = "Error floor0, reset mgc_option error"

	#this adds to the enemys stats based on players XP and
	enn1.MAXATK += int(.075 * MainPlayer.TOTALXP)
	enn1.MINATK += int(.075 * MainPlayer.TOTALXP)
	enn1.MHP += int(.015 * MainPlayer.TOTALXP)
	enn1.HP += int(.015 * MainPlayer.TOTALXP)
	enn1.ARM += int(.01 * MainPlayer.TOTALXP)
	MINPATK = str(
	 int(MainPlayer.WEP.mindam + (0.002 * (MainPlayer.TOTALXP / 10)) +
	     MainPlayer.STR))
	MAXPATK = str(
	 int(MainPlayer.WEP.maxdam + (0.002 * (MainPlayer.TOTALXP / 10)) +
	     MainPlayer.STR))
	MINEATK = str(int(enn1.MINATK + (.075 * MainPlayer.TOTALXP)))
	MAXEATK = str(int(enn1.MAXATK + (.075 * MainPlayer.TOTALXP)))

	#actual fight code
	#repeat so long as the enemy is alive
	while (enn1.HP > 0):
		#if the player dies
		if (MainPlayer.HP <= 0):
			os.system('clear')
			print("G A M E   O V E R \n you died to", enn0, "\n", enn1.DeMe)
			time.sleep(1800)

		#variables for the fight
		pdam = 0
		rdam = 0
		raw_to_hit = int(random.randint(1, 20))
		to_hit = int(random.randint(1, 20) + (0.055 * (Kill_Count / 9)))
		patk = int(
		 random.randint(MainPlayer.WEP.mindam, MainPlayer.WEP.maxdam) +
		 (.02 * MainPlayer.TOTALXP) + MainPlayer.STR)
		rdam = random.randint((enn1.MINATK + (0.075 * (MainPlayer.TOTALXP))),
		                      (enn1.MAXATK + (0.075 * (MainPlayer.TOTALXP))))
		HEAL = 0

		#menu on what kind of attack to do
		move = "False"
		if (MainPlayer.HoldLevel < 0):
			move = "True"
			MainPlayer.HoldLevel += 1
		while (move == "False"):
			os.system('clear')
			#this states the enemys name and stats
			PrintStats(MainPlayer)
			move = input(
			 "\n\n Attack(1)\n Magic(2)\n Burst and Hold(3)\n Inventory(4)\n")
			os.system('clear')

			#if you choose to Attack
			while (move == "1"):

				#adding blind to the menu if enough enemies have been killed
				if (Kill_Count > 8):
					PrintStats(MainPlayer)
					atk_option = input(
					 "\n \n what attack do you want to do? \n ATTACK(1)\n  \n PARRY(chance of failing)(2)\n BLIND ENEMY(3)\n BACK(N)\n"
					)
					os.system('clear')
				#start menu
				else:
					PrintStats(MainPlayer)
					atk_option = input(
					 "\n \n what attack do you want to do? \nATTACK(1), \nPARRY(chance of failing)(2), \nBack(N)\n"
					)
					os.system('clear')
				#registering if blind is on cooldown
				if (enemy_blind == "T1" and atk_option == "7"):
					PrintStats(MainPlayer)
					print("Blind is on cool down, can't use this turn or net \n")
					move = "False"
					time.sleep(5)
					os.system('clear')
				elif (enemy_blind == "T2" and atk_option == "7"):
					PrintStats(MainPlayer)
					print("Blind is on cool down, can't use this turn or net \n")
					move = "False"
					time.sleep(5)
					os.system('clear')

				#registering if the player wants to go back
				if (atk_option.capitalize() == "N"):
					move = "False"
					os.system('clear')

				#basic attack
				elif (atk_option == "1"):
					BasicAtk(MainPlayer)
					move = "True"

				#parry
				if (atk_option == "2"):
					Parry(MainPlayer)
					move = "True"

				#blind
				elif (atk_option == "3" and Kill_Count >= 8):
					Blind()
					move = "True"
				elif (atk_option == "3" and Kill_Count < 8):
					move = "1"

			time.sleep(0)  #this is here to stop below line from colapsing
			#if you choose to do Magic
			while (move == "2"):
				PrintStats(MainPlayer)
				mgc_option = input(
				 "\n\nWhat spell would you like to cast?\n heal(1) \n magic bolt(2) \nember(3) \n water spray(4) \n back(N)\n"
				)
				#back
				if (atk_option.capitalize() == "N"):
					os.system('clear')
					move = "False"

				#heal
				elif (mgc_option == "1"):
					MgcHealing(MainPlayer)
					move = "True"

				#magic bolt
				elif (mgc_option == "2"):
					MgcBolt(MainPlayer)
					move = "True"

				#ember, need to have residue damage
				elif (mgc_option == "3"):
					MgcEmber(MainPlayer)
					move = "True"

				#Water spray
				elif (mgc_option == "4"):
					MgcGlacialBlast(MainPlayer)
					move = "True"

				#back
				else:
					os.system('clear')
					move = "False"

			#burst and hold
			time.sleep(0)
			#if you Hold or Burst
			while (move == "3"):
				PrintStats(MainPlayer)
				hold_option = input(" Hold(1)\n Burst(2)\n cancel(N)\n")
				#canceled
				if (hold_option.capitalize() == "N"):
					move = "False"
				#Hold
				elif (hold_option == "1" and MainPlayer.HoldLevel < 5):
					Hold(MainPlayer)
					move = "True"
				elif (hold_option == "1" and MainPlayer.HoldLevel >= 5):
					print("Can't hold, your burst/hold level is maxed out, burst to lower it")
					time.sleep(4)
					move = "False"
				#Burst
				elif (hold_option == "2"):
					try:
						BurstAmmount = int(
					 input(
					  "How many times would you like to burst? Numbers only or this will crash\n"
					 ))
					except ValueError:
						move = "3"
					if (BurstAmmount <= MainPlayer.HoldLevel):
						Burst(MainPlayer)
						move = "True"
					elif (BurstAmmount < MainPlayer.HoldLevel):
						print(
						 "Your burst/hold level is",
						 MainPlayer.HoldLevel + ", however you tried to burst", BurstAmmount,
						 "times. Try a time that is less than or equal to your burst/hold level."
						)
						time.sleep(5)
						move = "False"
					else:
						move = "False"
				else:
					move = "False"

			time.sleep(0)
			#If you show your progress
			while (move == "4"):
				while move != "":
					print(PlayerData.SaveData)
					move = input("Press enter to continue")
					os.system('clear')
			time.sleep(0)

			#easter eggs
			while (move == "gay"):
				import eggs.the_big_gay
				time.sleep(30)
				os.system('clear')
				move = "False"
			while (move == "Garlic Bread"):
				import eggs.GoblinMace
				Gob_Mace_Taken == eggs.GoblinMace.Gob_Mace_Taken
				if (Gob_Mace_Taken == True):
					MainPlayer.WEP = equipment.weapons.gob_mace_shield
				move = "False"
#Save
			while (move.capitalize() == "Save"):
				SaveName = input("What would you like to name your save?")
				SaveName = f"saves/{SaveName}.txt"
				saves.SaveAndLoad.Save(SaveName, PlayerData.SaveData)
				move = False

#Load
			while (move.capitalize() == "Load"):
				SaveName = ""
				while SaveName == "" or os.path.exists(f"saves/{SaveName}.txt") == False:
					os.system('clear')
					SaveName = input("What is the name of your save file?")
				SaveName = f"saves/{SaveName}.txt"
				saves.SaveAndLoad.Load(SaveName)
				#Loading of data
				MainPlayer.NAME = PlayerData.SaveData["MPNAME"]
				MainPlayer.TOTALXP = PlayerData.SaveData["MPTXP"]
				MainPlayer.HP = PlayerData.SaveData["MPHP"]
				MainPlayer.MHP = PlayerData.SaveData["MPMHP"]
				MainPlayer.EXP = PlayerData.SaveData["MPEXP"]
				MainPlayer.STR = PlayerData.SaveData["MPSTR"]
				MainPlayer.ARC = PlayerData.SaveData["MPARC"]
				MainPlayer.FRES = PlayerData.SaveData["FRES"]
				MainPlayer.IRES = PlayerData.SaveData["IRES"]
				MainPlayer.ARES = PlayerData.SaveData["ARES"]
				MainPlayer.ERES = PlayerData.SaveData["ERES"]
				MainPlayer.PRES = PlayerData.SaveData["PRES"]
				GP = PlayerData.SaveData["gold"]
				Kill_Count = PlayerData.SaveData["KC"]
				WepCheck()
				ArmCheck()
				#reset to attack and stuff
				move = "False"

#settings
			while (move == "S"):
				import settings
				move = "False"

		#clear for report
		os.system('clear')
		PrintStats(MainPlayer)

		#apply armor
		"""
		#player armor/evasion
		if((MainPlayer.DEF+PlayerArmor.DEF) >= (MainPlayer.EVA+PlayerArmor.EVA)):
			rdam -= (MainPlayer.DEF+PlayerArmor.DEF)
		elif((MainPlayer.DEF+PlayerArmor.DEF) < (MainPlayer.EVA+PlayerArmor.EVA)):
			rdam -= (MainPlayer.EVA+PlayerArmor.EVA)
		#rat armor/evasion
		if(enn1.ARM >= enn1.EVA):
			pdam -= enn1.ARM
		elif(enn1.ARM < enn1.EVA):
			pdam -= enn1.EVA
	 """
		#make sure damage is greater than 0
		if (pdam < 0):
			pdam = 0
		if (rdam < 0):
			rdam = 0

	#deal and take the damage
		enn1.HP -= int(pdam)
		MainPlayer.HP -= int(rdam)

		#elemental damage
		apply_element_effects(EnemyList)
		apply_element_effects(PlayerList)
		#damage/health dealt/taken/gained
		if (MainPlayer.HP > 0):
			#if(to_hit == 20):
			#print("CRITICAL HIT \n")
			if (mgc_option == "1"):
				tatk = rdam
				tatk -= HEAL
				HEAL -= rdam
				print("\nPlayer healded", HEAL)
				tatk = min(0, 999999)
				print("You took", tatk, "damage")
				time.sleep(2)
			elif (mgc_option != "1"):
				print("\nPlayer delt", pdam)
				print("You took", rdam, "damage")
				time.sleep(2)
		os.system('clear')

	#when fight is over
	MainPlayer.EXP += enn1.XP
	GP += random.randint(enn1.MINGP, enn1.MAXGP)
	print("fight", Kill_Count, "over \n xp:", MainPlayer.EXP)
	Kill_Count += 1
	time.sleep(1.25)
	os.system('clear')

	#setting up varriables for next fight
	floor = int(Kill_Count / 10)  #the floor num goes up every 5 levels
	MainPlayer.HP += (.5 * Kill_Count)  #HP system, add 1 per 2 Kill_Count
	MainPlayer.HP = max(0, min(MainPlayer.HP, MainPlayer.MHP))
	patk = int(5 + (.002 * Kill_Count))  #this is the atk damage of the player

	#Updating save data
	PlayerData.SaveData = {
	 "MPNAME": MainPlayer.NAME,
	 "MPTXP": MainPlayer.TOTALXP,
	 "MPHP": MainPlayer.HP,
	 "MPMHP": MainPlayer.MHP,
	 "MPEXP": MainPlayer.EXP,
	 "MPWeapon": MainPlayer.WEP.NAME,
	 "MPArmor": MainPlayer.ARM.NAME,
	 "MPSTR": MainPlayer.STR,
	 "MPARC": MainPlayer.ARC,
	 "FRES": MainPlayer.FRES,
	 "IRES": MainPlayer.IRES,
	 "ARES": MainPlayer.ARES,
	 "ERES": MainPlayer.ERES,
	 "PRES": MainPlayer.PRES,
	 "gold": GP,
	 "KC": Kill_Count
	}
