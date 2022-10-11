
class Mage:
    def __init__(self) -> None:
        self.mage_health = 75
        self.mage_IQ = 50
        self.mage_mana = 75

    def getMageHealth(self):
        return self.mage_health()
    def getMageIQ(self):
        return self.mage_IQ()
    def getMageMana(self):
        return self.mage_mana()