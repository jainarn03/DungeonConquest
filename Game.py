from re import IGNORECASE
import time
import sys
import random
from tkinter import W


timea = 0.3
timeb = 0
#timeb = 0.04

def word(i):
    for character in i:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(timeb)
    time.sleep(timea)

def choiceMage(name):
    print("mage")
    mage1 = f"I see you like mages{name}, me too!"
    mage2 = "Now before we move forward let me explain how exactly the dungeons work"
    mage3 = "There are a total of 10 floors in this dungeon and the monsters will get harder each floor\nYou must survive all 10 floors and kill the Final Boss for the Trophy!"
    mage4 = "As a mage you will have the following attributes:\nHealth: 75, If your health drops to 0 then you will die and have to restart that floor\nIQ: 25, This is the amount of damage each spell will be based on\nMana: 50, You have limited mana so pick your spells wisely, if you run out of mana mid fight you die\nSpecial ability called Soul drain"
    mage5 = f"When you slect which spell you wish to use, 2 dices will be rolled\nIf the dices roll 2 - 6 then 50% of the IQ damage will be delt\nIf the dices roll a 7 - 11 then 90% of the IQ damage will be dealt\n If the dices roll a 12 then the special ability (Soul Drain) will be used and do the max damage possible"
    mage6 = "To begin with you will recive 3 spells\n>Zap (Does the same amount of damage as your IQ attribute and takes 20 mana)\n>Fireball (Does IQ + 10 damage but takes 30 mana)\nEarthquake (Does IQ + 25 damage but takes 40 mana)"
    mage7 = "At the end of each floor you may enter the shop and purchase better equipment using jerry coins"
    mage8 = f"I hope you now understand how the dungeon works{name}, Now go and get that trophy!"

def choiceWarrior(name):
    print("war")
    war1 = f"I see you like warriors{name}, good pick!"
    war2 = "Now before we move forward let me explain how exactly the dungeons work"
    war3 = "There are a total of 10 floors in this dungeon and the monsters will get harder each floor\nYou must survive all 10 floors and kill the Final Boss for the Trophy!"
    war4 = "As a warrior you will have the following attributes:\nHealth: 100, If your health drops to 0 then you will die and have to restart that floor\nStrength: 35, This is the amount of damage each hit will do to the monsters\nSpecial ability called Enchanted Shuriken"
    war5 = f"When you slect which move you wish to use, 2 dices will be rolled\nIf the dices roll 2 - 6 then you will lose 10% of your overlall health\nIf the dices roll a 7 - 11 then you lose 5% of your overall health\n If the dices roll a 12 then the special ability (Enchanted Shuriken) will be used and do the max damage possible"
    war6 = f"To begin with you will recive 3 moves\nWeapon throw (Does the same amount of damage as your strength attribute)\nCharge (Does strength + 20 damage but you lose +5% of your overall health)\nBlood bath (Does strength + 30 damage but you lose +10% of your overall health)"
    war7 = "At the end of each floor you may enter the shop and purchase better equipment using jerry coins"
    war8 = f"I hope you now understand how the dungeon works{name}, Now go and get that trophy!"

def intro():
    intro1 = "Hello there!\n"
    intro2 = "Welcome to the world of Dungeon conquest\n"
    intro3 = "You can call me Jerry!\n"
    intro4 = "Let me quickly explain to you how Dungeon Conquest works\n"
    intro5 = "You will take on a range of dungeons and bosses\n"
    intro6 = "You will gradually receive better gear to help you in combat as the dungeons will get harder\n"
    intro7 = "After you beat each dungeon, you will be rewarded with:\n"
    intro8 = "\t--> Jerry coins which can be used to buy better weapons/spells from the shop\n"
    intro9 = "\t--> skills point which can be used to level up your character attributes\n"
    intromage = "Mage Attributes:\nHealth: 75\nIQ: 25\nMana: 50"
    space = "\n======================================"
    introwarrior = "Warrior Attributes:\nHealth: 100\nStrength: 35"
    word(intro1)
    word(intro2)
    word(intro3)
    word(intro4)
    word(intro5)
    word(intro6)
    word(intro7)
    word(intro8)
    word(intro9)
    print(space)
    word(intromage)
    print(space)
    word(introwarrior)
    print(space)

def choice():
    introchoice = "Please pick your class (Mage OR Warrior): "
    introname = "What would you like me to call you: "
    word(introchoice)
    choice = input("")
    print(choice)
    word(introname)
    name = input()
    if choice.lower() == "mage" or "m":
        choiceMage(name)
    elif choice.lower() == "w" or "warrior":
        choiceWarrior(name)
    else:
        print("Fuck you")


choice()