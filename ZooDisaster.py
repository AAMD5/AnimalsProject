from Animal import *

grass = Grass()
leaves = Leaves()
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

# Input 

# "fox,bug,chicken,grass,sheep" 

# 1, fox can't eat bug, "fox,bug,chicken,grass,sheep" 
# 2, bug can't eat anything, "fox,bug,chicken,grass,sheep" 
# 3, chicken eats bug, "fox,chicken,grass,sheep" 
# 4, fox eats chicken, "fox,grass,sheep" 
# 5, fox can't eat grass, "fox,grass,sheep" 
# 6, grass can't eat anything, "fox,grass,sheep" 
# 7, sheep eats grass, "fox,sheep" 
# 8, fox eats sheep, "fox" 
# Output 
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", 
#  "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"] 

Zoo = [fox, bug, chicken, grass, sheep]

def AnimalsToStrings(listOfAnimals):
    ZooStrings = []
    for animal in listOfAnimals:
        ZooStrings.append(animal.value)
        
    return ZooStrings

def animalEat(zooList):
    zooListLength = len(zooList)
    for i in range(zooListLength): # from fox to sheep inclusive
        if zooList[i].eat(zooList[i-1])[0] == True and i != 0:
            #print(zooList[i].value)
            print(zooList[i].eat(zooList[i-1])[1])
            zooList.remove(zooList[i-1])
            print(AnimalsToStrings(zooList))
            break
        
        i = 0
        if zooList[i].eat(zooList[i+1])[0] == True:
            #print(zooList[i].value)
            print(zooList[i].eat(zooList[i+1])[1])
            zooList.remove(zooList[i+1])
            print(AnimalsToStrings(zooList))
            break

while len(Zoo) > 0:
    animalEat(Zoo)
    if len(Zoo) == 1:
        break