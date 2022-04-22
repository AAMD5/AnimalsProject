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

Zoo = [fox, chicken, sheep, panda, leaves, grass]

def AnimalsToStrings(listOfAnimals):
    ZooStrings = []
    for animal in listOfAnimals:
        ZooStrings.append(animal.value)
        
    return ZooStrings

# if panda.eat(grass)[0] == True:
#     print(panda.eat(grass)[1])
# else:
#     print(panda.eat(grass)[1])

length = len(Zoo)
for i in range(0, length):
    if Zoo[i].eat(Zoo[i+1])[0] == True:
        print(Zoo[i].value + " eats " + Zoo[i+1].value)
        Zoo.remove(Zoo[i+1])
        print(AnimalsToStrings(Zoo))
        
# if Zoo[0].eat(Zoo[1])[0] == True:
#     print(Zoo[0].value + " eats " + Zoo[1].value)
#     Zoo.remove(Zoo[1])
#     print(AnimalsToStrings(Zoo))