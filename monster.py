import random

#testing mode change after
def chance(x, y):
    rand = random.randint(x, y)
    print(rand)
    if rand == 1:
        print("Dodge")
    else:
        pass

class bat:
    def __init__(self):
        self.health = 50
        self.force = 35
        self.dodge = chance(1, 200)

class spider:
    def __init__(self):
        self.health = 75
        self.force = 50
        self.dodge = chance(1, 100)

class zombie:
    def __init__(self):
        self.health = 115
        self.force = 70
        self.dodge = chance(1, 50)

class goblin:
    def __init__(self):
        self.health = 150
        self.force = 95
        self.dodge = chance(1, 25)

class barryallen:
    def __init__(self):
        self.health = 250
        self.force = 100
        self.dodge = chance(1, 4)

class iris:
    def __init__(self):
        self.health = 260
        self.force = 125
        self.dodge = chance(1, 10)

class scarecrow:
    def __init__(self):
        self.health = 310
        self.force = 140
        self.dodge = chance(1, 8)

class vampire:
    def __init__(self):
        self.health = 350
        self.force = 165
        self.dodge = chance(1, 7)

class witch:
    def __init__(self):
        self.health = 390
        self.force = 185
        self.dodge = chance(1, 6)

class jerry:
    def __init__(self):
        self.health = 500
        self.force = 250
        self.dodge = chance(1, 5)