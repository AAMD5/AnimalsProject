from re import X
from Animal import *

# creating all objects


grass = Grass()
leaves = Leaves()
#################### name, color, age, speed, isDead, weight
antelope = Antelope("Antelope", "black", 5, 20, False, 20)
bigfish = Bigfish("Big-fish", "black", 5, 20, False, 20)
littlefish = Littlefish("Little-fish", "black", 5, 20, False, 20)
bug = Bug("Bug", "black", 5, 20, False, 20)
chicken = Chicken("Chicken", "black", 5, 20, False, 20)
cow = Cow("Cow", "black", 5, 20, False, 20)
sheep = Sheep("Sheep", "black", 5, 20, False, 20)
bear = Bear("Bear", "black", 5, 20, False, 20)
fox = Fox("Fox", "black", 5, 20, False, 20)
giraffe = Giraffe("Giraffe", "black", 5, 20, False, 20)
lion = Lion("Lion", "black", 5, 20, False, 20)
panda = Panda("Panda", "black", 5, 20, False, 20)

def AnimalsToStrings(listOfAnimals):
    
    """ changes list of animal objects to list of animal names """
    
    ZooStrings = []
    for animal in listOfAnimals:
        ZooStrings.append(animal.value)
        
    return ZooStrings

def animalEat(zooList):
    
    """ function that dictates which animal eats which prey """
    
    zooListLength = len(zooList)
    output = [AnimalsToStrings(zooList)]
    lastAnimal = False 
    while not lastAnimal:
        for i in range(zooListLength): # from fox to sheep inclusive
            if zooList[i].eat(zooList[i-1])[0] == True and i != 0:
                ateAnimal = zooList[i].eat(zooList[i-1])[1] 
                output.append(ateAnimal)
                print(AnimalsToStrings(zooList))
                print("Animal eaten to the left:", ateAnimal)
                zooList.remove(zooList[i-1]) # remove left eaten animal
                break # reset loop to stop animal eating more animals to the left
            
            elif zooList[i].eat(zooList[i+1])[0] == True and i <= zooListLength:
                ateAnimal = zooList[i].eat(zooList[i+1])[1]
                output.append(ateAnimal) 
                print(AnimalsToStrings(zooList))
                print("Animal eaten to the right:", ateAnimal)
                zooList.remove(zooList[i+1]) # remove right eaten animal
                break # reset loop to stop animal eating more animals to the right
            
            else:
                print(AnimalsToStrings(zooList))
                print("no edible animal left or right for the", zooList[i].value)
            
        if len(zooList) == 1: # last animal/s left
            output.append(AnimalsToStrings(zooList))
            lastAnimal = True  
            
    return output
     
Zoo = [fox, bug, chicken, grass, sheep]   
print("\nFinal output is", animalEat(Zoo))