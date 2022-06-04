
from generalAnimalClass import animalKind
import random

class specificAnimalClass:
    #t -> terrain
    def __init__(self, name, generalClass,t, currentPos, mother = None, father = None, reproduce_prob = .2,age = 0, thirst = 100, hunger = 100, age_limit = 100):
        self.name = name
        self.generalClass = generalClass
        self.currentPos = currentPos
        self.t = t
        self.sex = random.choices(["Male", "Female"])[0]
        self.mother = mother
        self.father = father
        self.age = age
        self.reproduce_prob = reproduce_prob
        self.thirst = thirst
        self.hunger = hunger
        self.age_limit = age_limit
        self.path = []
        self.pastPartners = []
        self.previousMove = None
        if self.mother == None:
            integer1, integer2 =  self.generalClass.speed_range[0],self.generalClass.speed_range[1]
            self.speed = random.randint(integer1, integer2)
        else:
            momSpeed = self.mother.speed
            dadSpeed = self.father.speed
            if momSpeed<=dadSpeed:
                self.speed = random.randint(momSpeed, dadSpeed)
            else:
                self.speed = random.randint(dadSpeed,momSpeed)

    #ADD SPEED
    
    #THE FOLLOWING FUNCTIONS WON'T BE AFFECTED BY CHANGES MADE TO THE TERRAIN CLASS

    def getReproduceProb(self):
        return self.reproduce_prob
    
    def getColor(self):
        return self.generalClass.getColor()
    
    def getGender(self):
        return self.sex

    def getCurrentPos(self):
        return self.currentPos

    def getName(self):
        return self.name

    def getGeneralClass(self):
        return self.generalClass

    def getAge(self):
        return self.age
    
    #THIS FUNCTION IS ABOUT HOW MUCH NUTRITION THE ANIMAL WILL GET ONCE IT EATS ITS PREY
    def nutritionLevel(self):
        a = self.thirst+self.hunger
        if a>100:
            a = 100
        return a

    def eat(self, prey):

        if prey == 'green':

            self.hunger = 100

        else:
            self.hunger+=prey.nutritionLevel()
            if self.hunger > 100:
                self.hunger = 100                
            self.t.kill(prey)

            i = prey.currentPos

            if len(self.t.assignment[i]) > 2:
                try:
                    self.t.assignment[i].remove(prey)
                except:
                    pass
            else:
                self.t.assignment[i][1] = None


    def drink(self):
        self.thirst = 100

    def reproduce(self, femalePartner):
        maleMoves = self.filterMoves(self.t.getPossibleMoves(self.currentPos))
        femaleMoves = self.filterMoves(self.t.getPossibleMoves(femalePartner.getCurrentPos()))
        self.reproduce_prob = 0
        femalePartner.setReproduceProb(0)
        self.pastPartners.append(femalePartner)
        femalePartner.pastPartners.append(self)
        if self.generalClass.maturityAge() < self.age and femalePartner.generalClass.maturityAge() < femalePartner.getAge():
            if len(maleMoves) != 0 or len(femaleMoves) != 0:
                    spawnPoint = None
                    for move in maleMoves+femaleMoves:
                        if self.t.getAssignment()[move][1] == None:
                            spawnPoint = move
                            break

                    if spawnPoint != None:
                        offSpring = specificAnimalClass("OFFSPRING OF "+str(self.name)+" and "+str(femalePartner.getName()),
                                                    self.generalClass,
                                                    self.t,
                                                    spawnPoint,
                                                    femalePartner,
                                                    self,
                                                    0.5)


                        return offSpring

        
    #Animal gets thirsty and hungry
    def changesAfterATurn(self):
        self.thirst -= self.generalClass.thirstRate()
        self.hunger -= self.generalClass.hungerRate()
        self.age += .1
        if self.reproduce_prob <= 1:
            self.reproduce_prob += .25
        if len(self.pastPartners) > 1:
            self.pastPartners.remove(self.pastPartners[0])

    def setReproduceProb(self,value):
        self.reproduce_prob = value

    def __str__(self):
        a = self.name+" is a "+self.generalClass.getSpecies()
        b = "Current Pos: "+ self.currentPos.__str__()
        c = "Sex: "+self.sex
        d = "Age: "+str(self.age)
        return "===================\n"+a+"\n"+b+"\n"+c+"\n"+d+"\n==================="

    def preysInList(self, liste):
        for animal in liste:
            try:
                if animal.getGeneralClass().getSpecies() in self.generalClass.getPreyList():
                    return animal
            except:
                if 'green' in self.generalClass.getPreyList():
                    return 'green'
         

#======================================
#THE FOLLOWING FUNCTIONS MIGHT BE AFFECTED BY CHANGES MADE TO THE TERRAIN FUNCITON
     
    def finding(self, vision):
        parents = []
        species = []
        predators = []
        preys = []
        waterCoord = []

        for coordinate in vision:
            for animal in vision[coordinate]:
                if type(animal) == specificAnimalClass:
                    if animal.getGeneralClass().getSpecies() in self.generalClass.getPreyList():
                        preys.append(coordinate)
                    if animal.getGeneralClass().getSpecies() in self.generalClass.getPredatorList(): 
                        predators.append(coordinate)
                    if animal.getGeneralClass().getSpecies() == self.generalClass.getSpecies():
                        species.append(coordinate)
                    if animal == self.mother or animal == self.father:
                        parents.append(coordinate)
            if vision[coordinate][0] == "blue":
                waterCoord.append(coordinate)
            
        return preys, predators, waterCoord, parents, species

    def shouldDie(self):
        if self.hunger <= 0 or self.thirst <= 0 or self.age >= self.age_limit:
            print(self.generalClass.getSpecies())
            if self.age>=self.age_limit:
                print('death from old age')
            if self.hunger<=0:
                print('death from hunger')
            if self.thirst<=0:
                print('death from thirst')
            return True

        return False

    def evaluate(self, pos):
            vision = self.t.seeWithinARadius(self.generalClass.getVisionRadius(), self.currentPos)
            value = 0
            a = self.finding(vision)
            preys = a[0]
            predators = a[1]
            waterCoord = a[2]
            parents = a[3]
            species = a[4]
            for i in waterCoord: 
                k = i.getManhattanDistance(pos)
                if k == 0:
                    k = 0.000001
                value += ((100-self.thirst)/10)*10*(1/k)
            for j in preys:
                k = j.getManhattanDistance(pos)
                if k == 0:
                    k = 0.000001
                value += ((100-self.hunger))*10*(1/k)
            for t in predators:
                value += t.getManhattanDistance(pos)
            if self.age < self.generalClass.maturityAge():
                for s in parents:
                    value += 20*s.getManhattanDistance(pos)
            for s in species:
                if self.generalClass.packAnimal():
                    value += s.getManhattanDistance(pos)
                #else:
                #    value -= s.getManhattanDistance(pos)
                
                #for i in self.t.assignment[s]:
                #    if type(i) != str and i != None:
                #        if i.sex != self.sex:
                #            value += self.reproduce_prob * s.getManhattanDistance(pos)                            
            
            value -= 5*self.path.count(pos)
            return value

    #Filters the moves based on if they are actually movable
    def filterMoves(self, moves):
        movables = []
        for i in moves:
            liste = self.t.assignment[i]
            if liste[0] != 'blue' and i not in movables:
                    movables.append(i)
        return movables

    def waterSource(self, moves):
        for i in moves:
            if self.t.getAssignment()[i][0] == "blue":
                return True
        return False

    def printPath(self):
        s = ''
        for i in self.path:
            s += i.__str__() + "-->"
        print(s)

    def move(self):
        moves = self.t.getPossibleMoves(self.currentPos)
        actualMoves = self.filterMoves(moves)
        l1 = len(actualMoves)
        if len(actualMoves)>1:
            if self.previousMove != None and self.previousMove in actualMoves:
                actualMoves.remove(self.previousMove)
        values = {}
        optimal = None
        storage = {}

        drinkProb = (100-self.thirst)/100
        prey = self.preysInList(self.t.assignment[self.currentPos])
        if 'green' == prey:
            if self.hunger<20:
                self.eat('green')
                return 'eaten1'
        else:
            for i in actualMoves:
                prey = self.preysInList(self.t.assignment[i])
                eatProb = (100-self.hunger)/100

                if prey!=None and  random.random()<eatProb:
                    self.eat(prey)
                    self.currentPos = i
                    self.t.animalList[self] = i
                    return 'eaten'


        if self.waterSource(moves):
            ranny = random.random()
            if ranny<drinkProb:
                self.drink()
                return "drink"
                  
        if self.sex == "Male":
                for i in moves:
                    for partner in self.t.assignment[i]:
                        if type(partner) != str and partner != None and partner.sex == "Female" and partner.getGeneralClass().getSpecies() == self.generalClass.getSpecies():
                            if self not in partner.pastPartners and partner not in self.pastPartners:
                                probability = self.reproduce_prob * partner.getReproduceProb()
                                if random.random() < probability:                                    
                                    child = self.reproduce(partner)
                                    print('reproduced')
                                    return child

        if len(actualMoves) != 0:
            for move in actualMoves:
                value = self.evaluate(move)
                values.update({value:move})
                storage.update({move:value})
                
            vision = self.t.seeWithinARadius(self.generalClass.getVisionRadius(), self.currentPos)
            a = self.finding(vision)
            Sum = 0
            for liste in a:
                Sum += len(liste)
            
            if Sum == 0:
                optimal = random.choice(actualMoves)
            else:
                    optimal = values[max(values)]
            self.previousMove = self.currentPos
            self.currentPos = optimal
            self.t.animalList[self] = self.currentPos

            self.path.append(self.currentPos)
            return "move"




        




