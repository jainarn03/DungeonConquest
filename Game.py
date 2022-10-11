import time
import sys
import random
from mage import Mage
import warrior as w


timea = 0.3
timeb = 0.01
#timeb = 0.04

def word(i):
    for character in i:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(timeb)
    time.sleep(timea)

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
    choice = input()
    print(choice)
    word(introname)
    name = input()
    if (choice.lower() == "m" or choice.lower() == "mage"):
        choiceMage(name)
    elif (choice.lower() == "w" or choice.lower() == "warrior" or choice.lower() == "war"):
        choiceWarrior(name)
    else:
        print("Fuck you")

def choiceMage(name):
    mage1 = f"I see you like mages {name}, me too!\n"
    mage2 = "Now before we move forward let me explain how exactly the dungeons work\n"
    mage3 = "There are a total of 10 floors in this dungeon and the monsters will get harder each floor\nYou must survive all 10 floors and kill the Final Boss for the Trophy!\n"
    mage4 = "As a mage you will have the following attributes:\n>Health: 75, If your health drops to 0 then you will die and have to restart that floor\n>IQ: 25, This is the amount of damage each spell will be based on\n>Mana: 50, You have limited mana so pick your spells wisely, if you run out of mana mid fight you die\n>Special ability called Soul drain\n"
    mage5 = f"When you slect which spell you wish to use, 2 dices will be rolled\nIf the dices roll 2 - 6 then 50% of the IQ damage will be delt\nIf the dices roll a 7 - 11 then 90% of the IQ damage will be dealt\nIf the dices roll a 12 then the special ability (Soul Drain) will be used and do the max damage possible\n"
    mage6 = "To begin with you will recive 3 spells\n>Zap (Does the same amount of damage as your IQ attribute and takes 20 mana)\n>Fireball (Does IQ + 10 damage but takes 30 mana)\n>Earthquake (Does IQ + 25 damage but takes 40 mana)\n"
    mage7 = "At the end of each floor you may enter the shop and purchase better equipment using jerry coins\n"
    mage8 = f"I hope you now understand how the dungeon works {name}, Now go and get that trophy!\n"
    word(mage1)
    word(mage2)
    word(mage3)
    word(mage4)
    word(mage5)
    word(mage6)
    word(mage7)
    word(mage8)

def mageGame():
    mHealth = Mage.mage_health()
    print(mHealth)


def choiceWarrior(name):
    war1 = f"I see you like warriors {name}, good pick!\n"
    war2 = "Now before we move forward let me explain how exactly the dungeons work\n"
    war3 = "There are a total of 10 floors in this dungeon and the monsters will get harder each floor\nYou must survive all 10 floors and kill the Final Boss for the Trophy!\n"
    war4 = "As a warrior you will have the following attributes:\n>Health: 100, If your health drops to 0 then you will die and have to restart that floor\n>Strength: 35, This is the amount of damage each hit will do to the monsters\n>Special ability called Enchanted Shuriken\n"
    war5 = f"When you slect which move you wish to use, 2 dices will be rolled\nIf the dices roll 2 - 6 then you will lose 10% of your overlall health\nIf the dices roll a 7 - 11 then you lose 5% of your overall health\nIf the dices roll a 12 then the special ability (Enchanted Shuriken) will be used and do the max damage possible\n"
    war6 = f"To begin with you will recive 3 moves\n>Weapon throw (Does the same amount of damage as your strength attribute)\n>Charge (Does strength + 20 damage but you lose +5% of your overall health)\n>Blood bath (Does strength + 30 damage but you lose +10% of your overall health)\n"
    war7 = "At the end of each floor you may enter the shop and purchase better equipment using jerry coins\n"
    war8 = f"I hope you now understand how the dungeon works {name}, Now go and get that trophy!\n"
    word(war1)
    word(war2)
    word(war3)
    word(war4)
    word(war5)
    word(war6)
    word(war7)
    word(war8)

mageGame()