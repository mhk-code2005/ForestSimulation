from generalAnimalClass import animalKind 
from specificAnimalClass import specificAnimalClass as animal
#green -> grass
deer = animalKind("deer",3,True,[1,1],["wolf","lion","cheetah",'deer'],["green"],1,1,"white", 4)
lion = animalKind("lion", 2, False, [1,3],['dragon'],["deer", "buffalo"],1, 2,"red", 3)
dragon = animalKind("dragon", 5, True, [1,4],[],["lion", 'deer','dragon'],1, 1,"grey", 3)

python = animalKind("python",3,False,(1,2),['eagle'],['wolf','frog','rat'],2,5,'orange',2)
eagle = animalKind('eagle',5,False, (1,5),[],['rat', 'python', 'wolf', 'frog'],1,10,'brown',2)
wolf = animalKind('wolf',2,True,(2,4),['python','eagle'],['rat','thrush'],2,2,'grey',2)
thrush = animalKind('thrush',3,True,(1,4),['wolf','eagle'],['fruitfly','dragonfly'],1,2,'bisque3',2)
frog = animalKind('frog',1,False,(3,4),['python'],['grasshopper','butterfly','fruitFly','dragonFly','green'],10,4,'aquamarine4',2)
dragonfly = animalKind('dragonfly',1,False,(1,1),['thrush','frog'],['butterfly','fruitfly'],10,10,'black',2)
butterfly = animalKind('butterfly',2,True,(1,1),['frog','dragonfly'],['green'],2,4,'chartreuse1',2)

sample1 = {deer:50,
          lion:3,
          dragon:4
        }
samples1 = list(sample1.keys())




sample2 = {python:3, 
            eagle:4,
            wolf:2, 
            thrush:5,
            frog:20,
            dragonfly:2,
            butterfly:5}

samples2 = list(sample2.keys())
