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

Zoo = [fox, bug, chicken, fox, grass, sheep, grass]

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
for i in range(length): # from fox to grass inclusive
    if Zoo[i].value == sheep.value:
        if Zoo[i-1].value == grass.value: # Animal eats to the left first
            print(Zoo[i].value + " eats " + Zoo[i-1].value)
            print(len(AnimalsToStrings(Zoo)))
            print("Animals list before left removal", AnimalsToStrings(Zoo))
            Zoo.remove(Zoo[i-1])
            print("Animals list after left removal", AnimalsToStrings(Zoo))
            break
        elif Zoo[i+1].value == grass.value: # Animal then eats to the right
            print(Zoo[i].value + " eats " + Zoo[i+1].value)
            print(len(AnimalsToStrings(Zoo)))
            print("Animals list before right removal", AnimalsToStrings(Zoo))
            Zoo.remove(Zoo[i+1])
            print("Animals list after right removal", AnimalsToStrings(Zoo))
            break
        


# for i in range(length):
#     if Zoo[i].value == sheep.value:
#         if Zoo[i-1].value == grass.value: # Animal eats to the left first
#             print(Zoo[i].value + " eats " + Zoo[i-1].value)
#             Zoo.remove(Zoo[i-1])
#             print(AnimalsToStrings(Zoo))

            
        # elif Zoo[i+1].value == grass.value:
        #     print(Zoo[i].value + " eats " + Zoo[i+1].value)
        #     Zoo.remove(Zoo[i+1])
        #     print(AnimalsToStrings(Zoo))
            
        # else:
        #     print(Zoo[i].value + " can't eat " + Zoo[i-1].value)
        #     print(AnimalsToStrings(Zoo))