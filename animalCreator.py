from generalAnimalClass import animalKind

def animalQuestion():
    species = input('Enter the name of the species: ')
    vision_radius = int(input("Enter the vision radius of the species: "))
    pack_animal = input("Is it a pack animal, yes or no:")
    if pack_animal == 'yes':
        pack_animal = True
    else:
        pack_animal = False
    print("Speed range is set to (1,4) as default")
    speed_range = (1,4)
    predator_list = [] 
    prey_list = []
    print("PREDATORS:")
    while True:
        print('=====')
        animal = input("Add a predator for this species; to stop, type 0_0: ")
        if animal != "0_0":
            predator_list.append(animal)
        else:
            break
    
    print("PREYS:  (NOTE: FOR GRASS, type green")
    while True:
        animal = input("Add a prey for this species; to stop, type 0_0: ")
        if animal != "0_0":
            predator_list.append(animal)
        else:
            break

    thirst_rate = 2
    hunger_rate = 2
    color = input("Enter a valid color that will represent the anima: l")
    maturity = int(input("Enter the maturity age: "))
    spec = animalKind(species,vision_radius,pack_animal,speed_range,predator_list,prey_list,thirst_rate, hunger_rate,color, maturity)
    return spec