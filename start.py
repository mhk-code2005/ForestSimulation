import time
import sample as smp
import animalCreator 
from graphics import visualizingTheSimulation





print()
print()
print()
print('|=|=|=|=|=|=||=|=|=|=|=|=||=|=|=|=|=|=||=|=|=|=|=|=||=|=|=|=|=|=||=|=|=|=|=|=||=|=|=|=|=|=|')
print("*** WELCOME TO THE FOREST SIMULATION ***")
print("Author: Mahir KAYA")
time.sleep(1)
print()
print('THE PURPOSE OF THIS PROJECT IS TO HAVE ANIMALS WITH DIFFERENT ATTRIBUTES\nSUCH AS AGE, PREYS, PREDATORS FROM DIFFERENT SPECIES INTERACT WITH EACH OTHER')   
time.sleep(1) 
print('WHILE THE SIMULATION IS RUNNING, THE NUMBER OF ANIMALS LEFT FROM A SPECIES WILL BE DISPLAYED IN A WINDOW')
time.sleep(1)
print()
print('THERE WILL ALSO BE A GRAPH THAT SHOWS THE POPULATION OF EACH SPECIES OVER TIME')
print()
print()

print("NOW, YOU WILL BE ASKED FOR YOUR PREFERENCES OF THE TERRAIN THAT IS A 30X30 GRID")

numberOfPuddles = int(input("Enter the number of puddles you want in the terrain: "))
puddles = {} # Center -> radius
for i in range(numberOfPuddles):
    print('----------')
    print("Puddle #"+str(i+1))
    xCenter = int(input("Enter the x coordinate of the center of the puddle: "))
    yCenter = int(input("Enter the y coordinate of the center of the puddle: "))
    radius = int(input('Enter the radius of the puddle: '))
    puddles.update({(xCenter,yCenter):radius})
print('----------')
print()
yesOrNo = int(input("Do you want to use the existing samples (enter 0) or create animals of your own (enter 1, although not recommended): "))

if yesOrNo == 0:
    print("Sample 1 consists of deers, lions and ,dragons")
    print("Sample 2 consists of more animals such as python, eagle, wolf, thrush, frog, dragon, butterfly")
    print("You can change how much of each animal will initially spawn by going to sample.py file")
    a = int(input("Enter the sample you want to use: "))
    if a == 1:
        sample = smp.sample1
        samples = smp.samples1
    
    else:
        sample = smp.sample2
        samples = smp.samples2

elif yesOrNo == 1:
    i = int(input("How many different types of animals do you want to add: "))
    sample = {}
    for t in range(i):
        spec = animalCreator.animalQuestion()
        a = int(input("How many times do you want this animal to be generated initially: "))
        sample.update({spec:a})
        samples = list(sample.keys())

else:
    print("Invalid Option")
    print("Quitting. . .")
    quit()

print("Finally . . .")
print("Do you want the forest to be visually represented as a grid, or do you just want to see the graph")
print("Visual representation makes the simulation go considerably slower")
a = input("Yes or No: ")
visualizingTheSimulation(sample, samples,a)

