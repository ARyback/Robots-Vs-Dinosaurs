from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_name, weapon_power):
        self.name = name
        self.health = 100
        self.weapon = Weapon(weapon_name, weapon_power)
        pass

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        pass


#Come back to line 7 later to undo the hard code adding parameters to init and names below

