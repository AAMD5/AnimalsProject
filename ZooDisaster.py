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
    for i in range(zooListLength): # from fox to sheep inclusive
        if zooList[i].eat(zooList[i-1])[0] == True and i != 0:
            ateAnimal = zooList[i].eat(zooList[i-1])[1] 
            zooList.remove(zooList[i-1]) # remove left eaten animal
            break # to stop animal eating more edible animals to the left
            
        i = 0 # reset loop
        if zooList[i].eat(zooList[i+1])[0] == True:
            ateAnimal = zooList[i].eat(zooList[i+1])[1]
            zooList.remove(zooList[i+1]) # remove right eaten animal
            break # to stop animal eating more edible animals to the right
        
            
    return ateAnimal
         
def eatStory(preys):
    
    """ story of which animal ate which prey """
    
    lastAnimal = False
    story = [AnimalsToStrings(preys)]
    while not lastAnimal:
        animalEatPrey = animalEat(preys)
        story.append(animalEatPrey)
        if len(preys) == 1: # only one animal left
            story.append(AnimalsToStrings(preys))
            lastAnimal = True

    return story
     
Zoo = [fox, bug, chicken, grass, sheep]   
print(eatStory(Zoo))