from coordClass import coordinate as coord
import random
from generalAnimalClass import animalKind 
from specificAnimalClass import specificAnimalClass as animal
import tkinter
from tkinter import *

class Terrain:
    def __init__(self, n):
        self.n = n
        self.terrain = [] #Set of coordinates
        self.assignment = {} # Format : {coord : [terrain_color, animal]}
        self.newAssignment = {} #Format : coord : [terrain_color, animal]
        self.animalList = {} # Format : {animal : coord}
        self.gridLabels = {}
        for i in range(n):
            liste = []
            for j in range(n):
                coordinate = coord(i,j)
                liste.append(coordinate)
                self.assignment.update({coordinate:[None,None]})
                self.newAssignment.update({coordinate:[None,None]})
            self.terrain.append(liste)

    #Prints out the coordinates in the terrain
    def printTerrain(self):
        for i in self.terrain:
            a = ""
            for j in i:
                a+= (j.__str__()+" ")
            print(a)
            print("\n")


    #Assigns the terrain based on the percentages given
    #To keep simulation simple, desertPercent, infertilePercent and grassPercent are set to 0 when actually coding
    #This might change in the future depending on the efficiency of the program

    def assignTerrain(self,waterPercent, desertPercent, grassPercent, infertilePercent, puddleList = {(15,15):5} ):
        if (waterPercent+desertPercent+grassPercent+infertilePercent!=100):
            print("INVALID PERCENTAGES")
        else:
            colors  = ["blue","yellow","green","orange"]
            weight = [waterPercent, desertPercent, grassPercent, infertilePercent] 
            for i in self.assignment:
                color = random.choices(colors, weights = weight)[0]
                self.assignment[i][0], self.newAssignment[i][0] = color , color

        def uniformWater(self):
            i= int(self.n/4)    
            s= 3*i
            for t in range(s-i):
                for q in range(s-i):
                    coordinate = self.terrain[i+t][i+q]
                    self.assignment[coordinate][0] = "blue"
                    self.newAssignment[coordinate][0] = "blue"

        #creates a circle pond in the middle of the terrain
        def circleWater(self, radius, center = (self.n/2, self.n/2)):
            
            s = center
            s1 = center[0]
            s2 = center[1]
            for t in range(self.n):
                for q in range(self.n):
                    coordinate = self.terrain[t][q]
                    if (t-s1)**2+(q-s2)**2 <= ((radius+.1)**2):
                        self.assignment[coordinate][0] = "blue"
                        self.newAssignment[coordinate][0] = "blue"

        for i in puddleList:
            circleWater(self, puddleList[i], i)

    #Initial function required to set labels with accurate colors using tkinter
    def visualizeTerrain(self, master):
            for i in range(len(self.terrain)):
                for b in range(len(self.terrain[i])):   
                    coordinate = self.terrain[i][b]
                    if (self.assignment[coordinate][1]==None):
                        q=Label(master, fg='white', bg=self.assignment[coordinate][0],  width=2, height=1,borderwidth=1, relief="groove")
                    else:
                        q=Label(master, fg='black', bg=self.assignment[coordinate][1].getColor(),  width=2, height=1,borderwidth=1, relief="groove")
                    self.gridLabels.update({coordinate:q})
                    q.grid(row=i,column=b)


    def getAssignment(self):
        return self.assignment

    def getPossibleMoves(self, coordinate):
        x = coordinate.getX()
        y = coordinate.getY()
        actualMoves = []
        possibleMoves = [(x,y+1), (x,y-1), (x+1,y), (x-1, y)]
        for move in possibleMoves:
            if 0<=move[0]<self.n and 0<=move[1]<self.n:
                coordin = self.terrain[move[0]][move[1]] 
                if coordin != coordinate:
                    actualMoves.append(coordin)
        return actualMoves

            
    #DELETE IF NOT USED BY THE END OF THE PROJECT
    def isValid(self, coord):
        if 0<coord.getX()<self.n and 0<coord.getY()<self.n:
            return True
        else:
            return False

    def seeWithinARadius(self, visionRadius, coordinate):
        vision = {}
        initPoint = (coordinate.getX()-visionRadius, coordinate.getY()-visionRadius)
        for i in range (1+2*visionRadius):
            for b in range(1+2*visionRadius):
                xVal , yVal= initPoint[0]+i, initPoint[1]+b
                if -1<xVal<self.n and -1<yVal<self.n:
                    coord2 = self.terrain[xVal][yVal]
                    vision.update({coord2:self.assignment[coord2]})
        vision.pop(coordinate)
        return vision

    def getN(self):
        return self.n

    def assignAnimal(self, pos, animal):
        if self.assignment[pos][1] == None:
            self.assignment[pos][1] = animal
        else:

            self.assignment[pos].append(animal)
        self.copy.update({animal:pos})
        #self.newAssignment[pos].append(animal)


    def updateAnimalList(self, animal, pos):
        if animal in self.animalList:
            self.animalList[animal] = pos
        else:
            self.animalList.update({animal:pos})

    def animalGenerator(self,generalClass, n):
        animals =  []
        for t in range(n):
            
            possibleCoords = []
            for i in self.assignment:
                if self.assignment[i][1] == None:
                    if self.assignment[i][0]!="blue":
                        possibleCoords.append(i)
            
            pos = random.choice(possibleCoords)
            possibleCoords.remove(pos)
            instance = animal(generalClass.getSpecies()+str(t), generalClass,self,pos,age = generalClass.maturityAge())
            self.assignment[pos][1] = instance
            self.animalList.update({instance:pos})

    def kill(self, Animal):
        self.animalList[Animal] = None
        for i in self.assignment:
            if Animal in self.assignment[i]:
                if len(self.assignment[i]) == 2:
                    self.assignment[i][1] = None
                else:
                    self.assignment[i].remove(Animal)

            if Animal in self.newAssignment[i]:
                if len(self.newAssignment[i]) == 2:
                    self.newAssignment[i][1] = None
                else:
                    self.newAssignment[i].remove(Animal)


    def oneTurn(self):
        children = []
        for Animal in self.animalList:
            if self.animalList[Animal] != None:

                if Animal.shouldDie():
                    self.kill(Animal)

                #HANDLES REPRODUCTION AND RECORDS THE MOVES OF ANIMALS
                else:
                    for i in range(Animal.speed):
                        coordinate = Animal.currentPos

                        a = Animal.move()
                        if type(a) == animal:
                            children.append(a)
                        self.animalList[Animal] = Animal.currentPos
                        if len(self.assignment[coordinate]) == 2:
                            self.assignment[coordinate][1] = None
                        else:
                            self.assignment[coordinate].remove(Animal)

                        Animal.changesAfterATurn()
                        if self.assignment[Animal.currentPos][1] == None:
                            self.assignment[Animal.currentPos][1] = Animal

                        else:
                            self.assignment[Animal.currentPos].append(Animal)

        #UPDATES THE ANIMAL LIST WITH BABIES
        for child in children:
            coordinate = child.getCurrentPos()
            if self.assignment[coordinate][1] == None:
                self.assignment[coordinate][1] = child
            else:
                self.assignment[coordinate].append(child)
            self.animalList.update({child:child.getCurrentPos()})



    def update(self ,master):

        widgets=master.winfo_children()
        for widget in widgets:
                if type(widget)==tkinter.Label:
                    coordinate = self.terrain[widget.grid_info()['row']][widget.grid_info()['column']]
                    widget.configure(bg = self.assignment[coordinate][0])
                    for anim in self.animalList:
                        if coordinate == self.animalList[anim]:
                            widget.configure(bg = anim.getColor())
                    
            
    
    def statistics(self, sample):
        stats = {i: 0 for i in sample}
        for k in self.animalList:
            if self.animalList[k] != None:
                stats[k.getGeneralClass()] += 1
        for i in stats:
            print(i.getSpecies(), ": ", stats[i])
        for i in self.animalList:
            print(i.getGeneralClass().getSpecies(),'at', self.animalList[i].__str__(), "age:", round(i.age,2), "hunger:", i.hunger, "thirst:", i.thirst, "gender:", i.sex)

