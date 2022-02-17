from herd import Herd
from fleet import Fleet
from random import randint

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dinosaur_index = randint(0, 2)
        self.robot_index = randint(0, 2)
        pass

    def run_game(self):
        self.display_welcome()
        self.battle(self.dinosaur_index, self.robot_index)
        pass

    def display_welcome(self):
        print("Are you ready to rumble?! Tonight we will see Dinosaurs versus Robots!")
        print("************************************")
        pass

    def battle(self, dinosaur_index, robot_index):
        while (self.fleet.robots[robot_index].health > 0 and self.herd.dinosaurs[dinosaur_index].health > 0):
            self.dino_turn(dinosaur_index, robot_index)
            self.robo_turn(robot_index, dinosaur_index)
            if self.fleet.robots[robot_index].health < 0:
                self.fleet.robots[robot_index].health = 0
            if self.herd.dinosaurs[dinosaur_index].health < 0:
                self.herd.dinosaurs[dinosaur_index].health = 0
            print(f"The health of the {self.herd.dinosaurs[dinosaur_index].name} is {self.herd.dinosaurs[dinosaur_index].health}.")
            print(f"The health of the {self.fleet.robots[robot_index].name} is {self.fleet.robots[robot_index].health}.")
            if (self.fleet.robots[robot_index].health <= 0 or self.herd.dinosaurs[dinosaur_index].health <= 0):
                if self.fleet.robots[robot_index].health == 0:
                    self.display_winners(self.herd.dinosaurs[dinosaur_index].name)
                elif self.herd.dinosaurs[dinosaur_index].health == 0:
                    self.display_winners(self.fleet.robots[robot_index].name)
                else: 
                    print("There was an error")
            pass

    def dino_turn(self, dinosaur_index, robot_index):
        self.herd.dinosaurs[dinosaur_index].attack(self.fleet.robots[robot_index])
        pass

    def robo_turn(self, robot_index, dinosaur_index):
        self.fleet.robots[robot_index].attack(self.herd.dinosaurs[dinosaur_index])
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self, winner):
        print(f"The winner is {winner}!")
        pass
