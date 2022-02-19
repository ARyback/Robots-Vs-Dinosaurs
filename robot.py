from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon_list = [Weapon("Laser", 15), Weapon("Lightsaber", 25), Weapon("Flamethrower", 35)]
        pass

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        pass

    def choose_weapon(self, user_choice):
        if user_choice == 0:
            self.weapon = self.weapon_list[0]
        elif user_choice == 1:
            self.weapon = self.weapon_list[1]
        elif user_choice == 2:
            self.weapon = self.weapon_list[2]
        else:
            print("There was an error!")


#Come back to line 7 later to undo the hard code adding parameters to init and names below

