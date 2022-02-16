from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = [Dinosaur("tim", 25), Dinosaur("jim", 15)]
        pass

    def create_herd(self):
        pass


# self.reptiles = [Dinosaur("tim", 25), Dinosaur("jim", 15)]
# herd = Herd()
# herd.dinosaurs.append(dinosaur)
# print(herd.dinosaurs[0].name) #it seems like it can only call specific properties not list items

# print(herd.reptiles[1].name, herd.reptiles[1].attack_power)
