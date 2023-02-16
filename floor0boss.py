import os
import random
import time
from Death_Messeges import *
from Death_Messeges2 import *
from player import *
#variables
Kill_Count = 9 #new Kill_Count every kill
floor = 0 #the floor num goes up every 5 levels
DeMe = "Death Messege, if you see this, there is an error"
enemy_name = "if you're seeing this, there is an error"
defcheck = 1
enemy_blind = "F"
sdmg = False
pdam = 0 #The amount of damage the player dealt this turn
rdam = 0 #The amount of damage the rat did to the player


print("B O S S   F I G H T")
time.sleep(1.5)
#Da Big Cheese Stats
DBCHP = 100
DBCATK = 22
DeMe = DBCDM
while(DBCHP > 0):
	enemy_name = "Da Big Cheese"
	print("Da Big Cheese \n")
	print("Kill_Count:", Kill_Count, "floor:", floor, "\n enemy hp:", DBCHP, "\n enemy atk:", DBCATK, "\n \n health:", PHP, "atk:", patk)
	action = input(str("\n \n what do you want to do? \n ATTACK(1), HEAL(2), DEFEND(3), DEFEND AND HEAL(4), PARRY(chance of failing)(5), DO NOTHING(6), BLIND(7) \n"))
	if (action == "1"):
		DBCHP -= patk
		pdam = patk
	elif (action == "2"):
		PHP += (random.randint(5, 15)+floor+Kill_Count)
		PHP = max(0, min(PHP, MPHP))
	elif (action == "4"):
		PHP += int((random.randint(5, 10)+(floor*Kill_Count)/2))
		PHP = min(PHP, MPHP)
	elif (action == "5"):
		parc = random.randint(1, 10)
		if (parc > 9):
			DBCHP -= 3*patk
			pdam = 3*patk
		elif (parc > 7):
			DBCHP -= 2*patk
			pdam = 2*patk
		elif (farc > 5):
			DBCHP -= patk
			PHP -= DBCATK
		elif (parc > 2):
			PHP -= DBCATK
		else:
			PHP -= 2*DBCATK
	elif (action == "3"):
		defcheck = random.randint(1, 10)
	elif (action == "6"):
		PHP -= DBCATK
	elif (action == "7" and Kill_Count >= 8):
			enemy_blind = "T1"
	if (Kill_Count == 8):
		print("YOU DISCOVERED ABILITY: BLIND")
	elif (action == "F1"):
		Kill_Count += 1
		patk += 50
	if (defcheck > 8):
			PHP -= DBCATK
			defcheck = 1
	if (action != "3" and action != "4" and DBCHP > 0 and action != "5" 	and action != "6" and enemy_blind != "T"):
		PHP -= DBCATK
	if (enemy_blind == "T2"):
		enemy_blind = "F"
	elif (enemy_blind == "T1"):
		enemy_blind = "T2"
	print("You dealt", pdam)
	print("The Big Cheese did", DBCATK, "damage")
	time.sleep(1.5)
	os.system('clear')
	
	if (PHP <= 0):
		os.system('clear')
		print("G A M E   O V E R \n you died to", enemy_name, "\n", DeMe)
		time.sleep(1800)
