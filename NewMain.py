#imports
import pygame, sys, random, os, time, sys, son, player, weapons, armor, RatClasses
from attacks import *
pygame.init()
#vairables
Version = "0.1.0 pre-alpha tests"
size = width, height = 1600, 800
fps = 60
black = 0, 0, 0
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Rats of Ruin')
fight = 0
Gob_Mace_Found = False
Gob_Mace_Taken = False
savedata = False
data_loaded = False
#attacks

#main game functions
def MenuScreen():
	global screen, version
	start = False
	greeting_screen = pygame.image.load('graphics/greet_screen/hello.png')
	screen.blit(greeting_screen, (-100, 0))
	pygame.display.update()
	#start code
	print("Welcome to Rat Souls! \n, This is going to suck, but always remember to have fun. \n (we do not take responsibility for any remotes, keyboards, or other items broken by the player due to rage, anger, and other strong emotions).\n \n WARNING: In combat, if you don't click a key with a designated output you will likely do aboslutely nothing for your turn but still take damage \n\n", Version, "\n\n")
	
	if(start == False):
		start = input("press ENTER to start \n")
		os.system('clear')
	screen.fill(black)
	pygame.display.flip()
	

#set up player
def BaseFloorFight():
	global Gob_Mace_Found, Gob_Mace_Found, MainPlayer, PlayerInventory, Kill_Count
	while MainPlayer.TOTALXP <= 50:
		from RatClasses import enn1
		if(MainPlayer.HP <= 0):
			os.system('clear')
			print("G A M E   O V E R \n you died to", enn1, "\n", enn1.DeMe)
		move = "error section A"
		atk_option = "error, section A"
		mgc_option = "error, section A"
		enn1.MAXATK += int((.5*MainPlayer.TOTALXP)+Kill_Count)
		enn1.MINATK += int((.5*Kill_Count)+floor)
		enn1.MHP += int(2*Kill_Count+(0.5*floor))
		enn1.HP += int(2*Kill_Count+(0.5*floor))
		enn1.ARM += int(.12*Kill_Count)
		
		
		

	
import NEWGAME
starterarmor = NEWGAME.PlayerArmor
starterweapon = NEWGAME.PlayerWeapon
MainPlayer = player.CharacterStats(NEWGAME.PLAYERNAME, 0, 125, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, starterweapon, starterarmor)
PlayerInventory = [starterweapon, starterarmor]


#game loop
while True:
	pygame.display.update()
	if fight == 0:
		BaseFloorFight()
		fight += 1