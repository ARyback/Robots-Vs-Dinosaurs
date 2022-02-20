from herd import Herd
from fleet import Fleet
from random import randint

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass

    def run_game(self):
        self.display_welcome()
        self.battle()
        pass

    def display_welcome(self):
        print("Are you ready to rumble?! Tonight we will see Dinosaurs versus Robots!")
        print("************************************")
        pass

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            dinosaur_index = randint(0, len(self.herd.dinosaurs) - 1)
            robot_index = randint(0, len(self.fleet.robots) - 1)
            self.skirmish(robot_index, dinosaur_index)
            self.battle_health_and_death(robot_index, dinosaur_index)
        self.battle_end()

    def health_check(self, robot_index, dinosaur_index):
        if (self.fleet.robots[robot_index].health == 0 or self.herd.dinosaurs[dinosaur_index].health == 0):
            if self.fleet.robots[robot_index].health == 0:
                self.display_loss(self.fleet.robots[robot_index].name)
            elif self.herd.dinosaurs[dinosaur_index].health == 0:
                self.display_loss(self.herd.dinosaurs[dinosaur_index].name)
            else: 
                print(f"There was an error!")

    def dino_turn(self, dinosaur_index, robot_index):
        self.herd.dinosaurs[dinosaur_index].attack(self.fleet.robots[robot_index])
        pass

    def robo_turn(self, robot_index, dinosaur_index):
        self.fleet.robots[robot_index].choose_weapon(int(input("Choose a weapon for the robot! Enter 0 to use a laser, 1 to use a light saber, and 2 to use a flame thrower.")))
        self.fleet.robots[robot_index].attack(self.herd.dinosaurs[dinosaur_index])
        pass

    def skirmish(self, robot_index, dinosaur_index):
        self.health_check(robot_index, dinosaur_index)
        self.dino_turn(dinosaur_index, robot_index)
        self.robo_turn(robot_index, dinosaur_index)

    def battle_health_and_death(self, robot_index, dinosaur_index):
        if self.fleet.robots[robot_index].health < 0:
            self.fleet.robots[robot_index].health = 0
        if self.herd.dinosaurs[dinosaur_index].health < 0:
            self.herd.dinosaurs[dinosaur_index].health = 0
        print(f"The health of the {self.herd.dinosaurs[dinosaur_index].name} is {self.herd.dinosaurs[dinosaur_index].health}.")
        print(f"The health of the {self.fleet.robots[robot_index].name} is {self.fleet.robots[robot_index].health}.\n")
        if self.fleet.robots[robot_index].health == 0:
            print(f"{self.fleet.robots[robot_index].name} robot is out of the game!")
            self.fleet.robots.pop(robot_index)
        if self.herd.dinosaurs[dinosaur_index].health == 0:
            print(f"{self.herd.dinosaurs[dinosaur_index].name} dinosaur is out of the game!")
            self.herd.dinosaurs.pop(dinosaur_index)

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_loss(self, loser):
        print(f"************")
        print(f"\nThe {loser} has zero health. It is out of the battle.\n")
        print(f"************")

    def battle_end(self):
        if len(self.fleet.robots) == 0:
            print(f"THE DINOSAURS WON THE FINAL BATTLE!")
        elif len(self.herd.dinosaurs) == 0:
            print(f"THE ROBOTS WON THE FINAL BATTLE!")
        else:
            print("There was an error!")
