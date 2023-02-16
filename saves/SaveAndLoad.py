import json, random, time, os, PlayerData
#here is a funcion for saving the data, can't find out how to take the dictionary out of a function so I can't have a load function
def Save(savefile, data):
	with open(savefile, 'w') as json_file:
		json.dump(data, json_file)

def Load(savefile):
	global PlayerData
	with open(savefile, 'r') as f:
		PlayerData.SaveData = json.load(f)

