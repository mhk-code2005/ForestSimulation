"""
DOES NOT NEED MODIFICATION
"""
class animalKind: 
    """
    pack_animal --> Boolean, whether or not the animal travels in packs
    speed_range --> Tuple, upper and lower limits of the speed an animal of this species can have
    thirst_rate --> How fast the animal becomes thirsty
    hunger_rate --> How fast the animal becomes hungry
    nutrition_level --> How much hunger points does the predator gets when he eats the prey
    """
    def __init__(self, species, 
                vision_radius, 
                pack_animal, 
                speed_range, 
                predator_list, 
                prey_list,
                thirst_rate,
                hunger_rate,
                color,
                maturity):
        self.species = species
        self.vision_radius = vision_radius
        self.pack_animal = pack_animal
        self.speed_range = speed_range
        self.predator_list = predator_list
        self.prey_list = prey_list
        self.thirst_rate = thirst_rate
        self.hunger_rate = hunger_rate
        self.color = color
        self.maturity = maturity

    def getColor(self):
        return self.color
    def getPreyList(self):
        return self.prey_list
    def getPredatorList(self):
        return self.predator_list
    def getSpecies(self):
        return self.species
    def getVisionRadius(self):
        return self.vision_radius
    def getSpecies(self):
        return self.species
    def maturityAge(self):
        return self.maturity
    def thirstRate(self):
        return self.thirst_rate
    def hungerRate(self):
        return self.hunger_rate
    def packAnimal(self):
        return self.pack_animal
    def __str__(self):
        return "species: "+ self.species
        
    