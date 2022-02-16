from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass

    def run_game(self):
        self.display_welcome()
        self.battle(1,2)
        self.display_winners()
        pass

    def display_welcome(self):
        print("Are you ready to rumble?! Tonight we will see Dinosaurs versss Robot!")
        print("************************************")
        pass

    def battle(self, dinosaur_index, robot_index):
        while (self.fleet.robots[robot_index].health > 0 or self.herd.dinosaurs[dinosaur_index].health > 0):
            self.dino_turn(dinosaur_index, robot_index)
            self.robo_turn(robot_index, dinosaur_index)
            print(f"The health of the {self.herd.dinosaurs[dinosaur_index].name} is {self.herd.dinosaurs[dinosaur_index].health}.")
            print(f"The health of the {self.fleet.robots[robot_index].name} is {self.fleet.robots[robot_index].health}.")
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

    def display_winners(self):
        print(f"Winners are always dinosaurs!")
        pass

