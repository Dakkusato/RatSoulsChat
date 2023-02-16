#imports
import time, os, pygame, json
#variables
player_image_selected = False
set_player_image = '/graphics/players/playert.png'
savedata = False
data_loaded = False
save_slot = False
load_slot = False
#lists
player_image_list = ["graphics/players/test.png"]
#libraries

#saved data
save_library = {"weapon": 5
	
}



#Save and load funcitions
def Save(savefile, savedata):
	with open(savefile, 'w') as json_file:
		json.dump(savedata, json_file)

def Load(savefile):
	global loadeddata
	with open(savefile, 'r') as f:
		loadeddata = json.load(f)

#Sprite classes
class ImageSprite(pygame.sprite.Sprite):
	def __init__(self, picture, width, height, pos_x, pos_y):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(picture)
		self.rect = self.image.get_rect()
		self.rect.center = (width/2, height/2)
		
#What to do
setting_choice_A = True
while setting_choice_A == True:
	setting_choice_A = input("What would you like to do?\n save(1)\n load(2)")
	if setting_choice_A == "1":
		while save_slot == False:
			save_slot == input("Which save slot? 1, 2, 3, or cancel(N)?")
			if(save_slot == "1"):
				Save('saves/saved_data1.txt', save_library)
			elif(save_slot == "2"):
				Save('saves/saved_data2.txt', save_library)
			elif(save_slot == "3"):
				Save('saves/saved_data3.txt', save_library)
			elif(save_slot.capitalize() == "N"):
				save_slot == "canceled"
			else:
				save_slot = False
		save_slot == False
		print("saved")
		time.sleep(5)

	#load data
	elif(setting_choice_A == "2"):
		while load_slot == False:
			load_slot == input("Which save slot? 1, 2, 3, or cancel(N)??")
			data_loaded = True
			if(load_slot == "1"):
				Load('saves/saved_data1.txt')
			elif(load_slot == "2"):
				Load('saves/saved_data2.txt')
			elif(load_slot == "3"):
				Load('saves/saved_data3.txt')
			elif(load_slot.capitalize() == "N"):
				load_slot = "Canceled"
				data_loaded = False
			else:
				load_slot = False
		load_slot = False

