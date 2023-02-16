import random, os, time, json, player, equipment.weapons, equipment.armor
from equipment.weapons import starter_weapon_list
from equipment.armor import starter_armor_list

#Player Name
PLAYERNAME = input("What is your name?\n")
if PLAYERNAME == "":
	PLAYERNAME = "Solar"
os.system('clear')

#select weapons
weapon_list_selected_option = 0
weapon = "none"
keep_looking_or_keep_weapon = "n"
while(weapon == "none"):
	print("Choose Your Weapon \n\n")
	weapon_list_selected_option = int(input(f"the weapon options are {1} to {len(starter_weapon_list)}. Which weapon would you like to see? \n"))
	
	os.system('clear')
	print(starter_weapon_list[weapon_list_selected_option-1].NAME + ": " + starter_weapon_list[weapon_list_selected_option-1].description)
		
		
	keep_looking_or_keep_weapon = input("type Y to keep this weapon, N to get keep looking \n")
	
	if(keep_looking_or_keep_weapon.capitalize() == "Y"):
		weapon = (weapon_list_selected_option-1)
		os.system('clear')
		
	elif(keep_looking_or_keep_weapon.capitalize() == "N"):
		weapon = "none"
		os.system('clear')

	else:
		weapon = "none"
		os.system('clear')

PlayerWeapon = starter_weapon_list[weapon]


#select armor
armor_list_selected_option = 0
armor = "none"
keep_looking_or_keep_armor = "n"
while(armor == "none"):
	print("Choose Your armor \n\n")
	armor_list_selected_option = int(input(f"the weapon options are {1} to {len(starter_armor_list)}. Which weapon would you like to see? \n"))
	
	if armor_list_selected_option == 1:
		os.system('clear')
		print(starter_armor_list[0].NAME + ": " + starter_armor_list[0].DESC)
		
	elif armor_list_selected_option == 2:
		os.system('clear')
		print(starter_armor_list[1].NAME + ": " + starter_armor_list[1].DESC)
		
	elif armor_list_selected_option == 3:
		os.system('clear')
		print(starter_armor_list[2].NAME + ": " + starter_armor_list[2].DESC)
		
	elif armor_list_selected_option == 4:
		os.system('clear')
		print(starter_armor_list[3].NAME + ": " + starter_armor_list[3].DESC)
		
	elif armor_list_selected_option == 5:
		os.system('clear')
		print(starter_armor_list[4].NAME + ": " + starter_armor_list[4].DESC)
		
	else:
		os.system('clear')
		armor = "none"
		
		
	keep_looking_or_keep_armor = input("type Y to keep this armor, N to get keep looking \n")
	
	if(keep_looking_or_keep_armor.capitalize() == "Y"):
		armor = (armor_list_selected_option-1)
		os.system('clear')
		
	elif(keep_looking_or_keep_armor.capitalize() == "N"):
		armor = "none"
		os.system('clear')

	else:
		armor = "none"
		os.system('clear')

PlayerArmor = starter_armor_list[armor]

player.MainPlayer = player.CharacterStats(PLAYERNAME, 0, 125, 125, 0, 0, 0, 0, 0, PlayerWeapon, PlayerArmor)