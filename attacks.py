import random, os, time
def BasicAtk(wep):
	global Kill_Count, mebonus, pdam, floor, Kill_Count, MainPlayer, to_hit, PlayerArmor, PlayerWeapon
	if(to_hit == (21-(20*wep.crit))):
		pdam += int(wep.crmult*patk+mebonus)
	elif(to_hit >= enn1.ARM):
		pdam += int(patk+mebonus)
		#animation = basic_attack_hit
	else:
		pdam += 0
		#animation = basic_attack_miss



def Parry(wep):
	global pdam, rdam
	parry_crit_success = 21-(20*wep.crit)
	parry_success = parry_crit_success-(20*wep.psuc)
	parry_part_success = parry_success-(20*wep.prtpsuc)
	parry_fail = parry_part_success-(20*wep.pfail)
	parry_crit_fail = parry_fail-(20*wep.pcrfail)
	

	parc = random.randint(1, 20)
	#animation = parry_fail
	
	if (parc >= (parry_crit_success)):
		rdam += 0
		pdam += int(wep.crmult*patk)
		#animation = parry_success
		
	elif (parc >= (parry_success)):
		rdam += 0
		pdam += int((.75*wep.crmult)*patk)
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
		print("error: floor0, parry_critical_fail, weapon:", wep, "please screenshot and save the screenshot, restart the game, and if this persists sent the screenshot to RatSouls@gmail.com asking for help")
		time.sleep(99999999999999)
	
	

def Blind():
	global enemy_blind, sdmg
	enemy_blind = "T1"
	sdmg = True
	if (Kill_Count == 8):
		print("YOU DISCOVERED ABILITY: BLIND")
	


def MgcHealing(wep, arm):
	global pdam, floor, Kill_Count, PHP, MPHP, HEAL
	if((wep.wbonus+arm.wbonus) >= (wep.grybonus+arm.grybonus)):
		HEAL = int((random.randint(8, 15)+floor+(Kill_Count/2))+wep.wbonus+arm.wbonus)
	if((wep.grybonus+arm.grybonus) < (wep.wbonus+arm.wbonus)):
		HEAL = int((random.randint(8, 15)+floor+(Kill_Count/2))+(wep.grybonus+arm.grybonus))
	PHP += HEAL
	PHP = max(0, min(PHP, MPHP))
	#animation = heal



def MgcBolt(wep, arm):
	global Kill_Count, pdam, floor, Kill_Count, to_hit, MainPlayer, enn1
	if(to_hit >= enn1.ARM):
		if((wep.bbonus+arm.bbonus) >= (wep.grybonus+arm.grybonus)):
			pdam = int(random.randint(3, 5)+(Kill_Count*0.002)+wep.bbonus+arm.bbonus)
		if((wep.bbonus+arm.bbonus) < (wep.grybonus+arm.grybonus)):
			pdam = int(random.randint(3, 5)+(Kill_Count*0.002)+wep.grybonus+arm.grybonus)
	else:
		pdam = int(0)



def MgcEmber(wep, arm):
	global pdam, floor, Kill_Count, PHP, MPHP
	if((wep.bbonus+arm.bbonus) >= (wep.grybonus+arm.grybonus) and (wep.bbonus+arm.bbonus) >= (wep.grnbonus+arm.grnbonus)):
		pdam += int(random.randint(2, 3)+(Kill_Count*0.002)+(wep.bbonus+arm.bbonus))
	if((wep.grybonus+arm.grybonus) > (wep.bbonus+arm.bbonus) and (wep.grybonus+arm.grybonus) > (wep.grnbonus+arm.grnbonus)):
		pdam += int(random.randint(2, 3)+(Kill_Count*0.002)+(wep.grybonus+arm.grybonus))
	if( (wep.grnbonus+arm.grnbonus) > (wep.bbonus+arm.bbonus) and  (wep.grnbonus+arm.grnbonus) > (wep.grybonus+arm.grybonus)):
		pdam += int(random.randint(2, 3)+(Kill_Count*0.002)+(wep.grnbonus+arm.grnbonus))
	



def MgcWaterSpray(wep, arm):
	global pdam, floor, Kill_Count, PHP, MPHP
	if((wep.bbonus+arm.bbonus) >= (wep.grybonus+arm.grybonus)):
		pdam = int(2+(Kill_Count*0.005)+wep.bbonus+arm.bbonus)
	if((wep.bbonus+arm.bbonus) < (wep.grybonus+arm.grybonus)):
		pdam = int(2+(Kill_Count*0.005)+(wep.grybonus+arm.grybonus))

							 
def Hold():
	global move, HoldLevel
	if HoldLevel < 5 and HoldLevel > -4:
		HoldLevel += 1
	else:
		move = False

def Burst(wep):
	global HoldLevel, Kill_Count, mebonus, pdam, patk, MainPlayer, enn1
	BrstAmt = int(input("How many times would you like to burst? numbers only or this will crash"))
	HoldLevel -= BrstAmt
	for x in range(BrstAmt):
		hit = int(random.randint(1, 20)+(0.055*(Kill_Count/9)))
		if(hit == (21-(20*wep.crit))):
			pdam += int(wep.crmult*patk+mebonus)
		elif(hit >= enn1.ARM and hit >= enn1.EVA):
			pdam += int(patk+mebonus)
			#animation = basic_attack_hit
		else:
			pdam += 0
			#animation = basic_attack_miss