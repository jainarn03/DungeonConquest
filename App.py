import time
import sys
import random


timea = 0.2
timeb = 0.04

def word(i):
    for character in i:
        sys.stdout.write(character)
        #sys.stdout.flush()
        time.sleep(timeb)
    time.sleep(timea)

def intro():
    intro1 = "Hello there!\n"
    intro2 = "Welcome to the world of Dungeon conquest\n"
    intro3 = "You can call me Jerry\n"
    intro4 = "Let me quickly explain to you how Dungeon Conquest works\n"
    intro5 = "You will take on a range of dungeons and bosses\n"
    intro6 = "You will gradually receive better gear to help you in combat as the dungeons will get harder\n"
    intro7 = "After you beat each dungeon, you will be rewarded with:\n"
    intro8 = "\t--> Jerry points which will level up your character\n"
    intro9 = "\t--> Jerry coins which can be used to buy better weapons/spells from the shop\n"
    intro0 = "\t--> skills point which can be used to level up your character attributes\n"
    introname = "What would you like me to call you: "
    introchoice = "Please pick your class(m/w):\nMage\nWarrior\n"
    word(intro1)
    word(intro2)
    word(intro3)
    word(intro4)
    word(intro5)
    word(intro6)
    word(intro7)
    word(intro8)
    word(intro9)
    word(intro0)
    word(introname)
    name = input()
    word(introchoice)
    choice = input()
    return name, choice

intro()
