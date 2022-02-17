#From battlefield
#  print("Current Dinosaur Turn: ")
#         dino_select = int(input(f"Press 0 to select {self.herd.dinosaurs[0].name} with {self.herd.dinosaurs[0].health} health.\nPress 1 to select {self.herd.dinosaurs[1].name} with {self.herd.dinosaurs[1].health} health.\nPress 2 to select {self.herd.dinosaurs[2].name} with {self.herd.dinosaurs[2].health} health.\n"))
#         if dino_select == 0:
#             dino_chosen = self.herd.dinosaurs[0].name
#         elif dino_select == 1:
#             dino_chosen = self.herd.dinosaurs[1].name
#         elif dino_select == 2:
#             dino_chosen = self.herd.dinosaurs[2].name
#         else:
#             print("You made an error!")
#         print(dino_chosen)

#  print("Current Robot Turn: ")
#         robo_select = int(input(f"Press 0 to select {self.fleet.robots[0].name} with {self.fleet.robots[0].health} health.\nPress 1 to select {self.fleet.robots[1].name} with {self.fleet.robots[1].health} health.\nPress 2 to select {self.fleet.robots[2].name} with {self.fleet.robots[2].health} health.\n"))
#         if robo_select == 0:
#             robo_chosen = self.herd.dinosaurs[0].name
#         elif robo_select == 1:
#             robo_chosen = self.herd.dinosaurs[1].name
#         elif robo_select == 2:
#             robo_chosen = self.herd.dinosaurs[2].name
#         else:
#             print("You made an error!")
#         print(robo_chosen)

#Battle while (self.fleet.robots[robot_index].health > 0 or self.herd.dinosaurs[dinosaur_index].health > 0):

# Currently works fine but without using extra dinosaurs
#     def battle(self, dinosaur_index, robot_index):
#         while (self.fleet.robots[robot_index].health > 0 and self.herd.dinosaurs[dinosaur_index].health > 0):
#             self.dino_turn(dinosaur_index, robot_index)
#             self.robo_turn(robot_index, dinosaur_index)
#             if self.fleet.robots[robot_index].health < 0:
#                 self.fleet.robots[robot_index].health = 0
#             if self.herd.dinosaurs[dinosaur_index].health < 0:
#                 self.herd.dinosaurs[dinosaur_index].health = 0
#             print(f"The health of the {self.herd.dinosaurs[dinosaur_index].name} is {self.herd.dinosaurs[dinosaur_index].health}.")
#             print(f"The health of the {self.fleet.robots[robot_index].name} is {self.fleet.robots[robot_index].health}.")
#             if (self.fleet.robots[robot_index].health <= 0 or self.herd.dinosaurs[dinosaur_index].health <= 0):
#                 if self.fleet.robots[robot_index].health == 0:
#                     self.display_winners(self.herd.dinosaurs[dinosaur_index].name)
#                 elif self.herd.dinosaurs[dinosaur_index].health == 0:
#                     self.display_winners(self.fleet.robots[robot_index].name)
#                 else: 
#                     print("There was an error")

