import os, PlayerData, player
import saves.SaveAndLoad
import equipment.armor
import equipment.weapons

#functions to check gear
def WepCheck():
	global PlayerData, MainPlayer
	for weapon in range(len(equipment.weapons.all_weapon_list)):
		WepName = str(PlayerData.SaveData["MPWeapon"])
		if WepName == equipment.weapons.all_weapon_list[weapon].NAME:
			player.MainPlayer.WEP = equipment.weapons.all_weapon_list[weapon]
		else:
			pass

def ArmCheck():
	global PlayerData, MainPlayer
	for armor in range(len(equipment.armor.all_armor_list)):
		WepName = PlayerData.SaveData["MPWeapon"]
		if WepName == equipment.armor.all_armor_list[armor].NAME:
			player.MainPlayer.ARM = equipment.armor.all_armor_list[armor]



#Load
move = "load"
while(move.capitalize() == "Load"):
	SaveName = ""
	while SaveName == "" or os.path.exists(f"saves/{SaveName}.txt") == False:
		os.system('clear')
		SaveName = input("What is the name of your save file?")
	SaveName = f"saves/{SaveName}.txt"
	saves.SaveAndLoad.Load(SaveName)
#Loading of data
	player.MainPlayer.NAME = PlayerData.SaveData["MPNAME"]
	player.MainPlayer.TOTALXP = PlayerData.SaveData["MPTXP"]
	player.MainPlayer.HP = PlayerData.SaveData["MPHP"]
	player.MainPlayer.MHP = PlayerData.SaveData["MPMHP"]
	player.MainPlayer.EXP = PlayerData.SaveData["MPEXP"]
	player.MainPlayer.STR = PlayerData.SaveData["MPSTR"]
	player.MainPlayer.ARC = PlayerData.SaveData["MPARC"]
	player.MainPlayer.FRES = PlayerData.SaveData["FRES"]
	player.MainPlayer.IRES = PlayerData.SaveData["IRES"]
	player.MainPlayer.ARES = PlayerData.SaveData["ARES"]
	player.MainPlayer.ERES = PlayerData.SaveData["ERES"]
	player.MainPlayer.PRES = PlayerData.SaveData["PRES"]
	GP = PlayerData.SaveData["gold"]
	Kill_Count = PlayerData.SaveData["KC"]
	WepCheck()
	ArmCheck()
	move = "FIN"