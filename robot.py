from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_power):
        self.name = name
        self.health = 0
        self.weapon = Weapon(input("Enter name: "), weapon_power)
        pass

    def attack(self, dinosaur):
        pass

