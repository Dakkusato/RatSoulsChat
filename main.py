import os
import random
import time
import pygame
from Death_Messeges import *
from Death_Messeges2 import *
from player import *

Version = "0.1.0 pre-alpha tests"

start = False
Kill_Count = 0
floor = int(Kill_Count/10)
DeMe = "Death Messege, if you see this, there is an error"
enemy_name = "if you're seeing this, there is an error"
defcheck = 1
enemy_blind = "F"
sdmg = False
pdam = 0
rdam = 0


#pygame starts
pygame.init()
os.system('clear')

size = width, height = 1600, 800
fps = 60
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rat Souls')

#menu screen
greeting_screen = pygame.image.load('graphics/greet_screen/hello.png')

screen.blit(greeting_screen, (-100, 0))
pygame.display.update()


#start code
def StartMessage():
    print("""Welcome to Rat Souls!
This is going to suck, but always remember to have fun.
(we do not take responsibility for any remotes, keyboards, or other items broken by the player due to rage, anger, and other strong emotions).

WARNING: In combat, if you don't click a key with a designated output you will likely do aboslutely nothing for your turn but still take damage

""", Version, "\n\n")

while not start:
    StartMessage()
    try:
        start = int(input("New Game(1)\nLoad Game(2)\n"))
    except ValueError:
        start = False
    if start == 1:
        os.system('clear')
        import saves.NEWGAME
        os.system('clear')
        start = True
    elif start == 2:
        os.system('clear')
        import saves.LOADGAME
        start = True
    else:
        start = False
        os.system('clear')

screen.fill(black)
pygame.display.flip()

"""
LEVEL 1
"""
import floor0

"""
LEVEL 2
"""

if floor0.Kill_Count >= 10:
    import floor0boss

DBSK = ""
print("i-")
time.sleep(0.1)
print("you... kill me...")

while not DBSK:
    DBSK = input("\x1B[3m he falls to the ground \x1B[0m NO... ME. WILL. LIVE!(enter to continue)")
    DBSK = True

os.system('clear')
print("you killed the first boss! nobody has defeated them since as long as our history goes back, good job! \n")
print("you discovered ability: DOUBLE ATTACK")
time.sleep(10)
os.system('clear')
print("Welp for the remaster that is all we are working on as of the moment, thank you for playing please leave your thoughts in comments or email me at RatSouls@gmail.com")
time.sleep(120)

"""
#level/boss 2
#print the "welcome to second floor" code
print("You begin to think to yourself about the fact that you have compleated a floor and proven yourself to be stronger than any before you, yet this is still just the begining.")
time.sleep(1.5)

import floor1

import floor1boss
from floor1boss import floor

#floor 3

"""
print("You... Made it this far? Impressive, worry not I shall update it later. Au Revoir")
time.sleep(3600)
print(f"Bro, you left the stuff on")