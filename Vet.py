from Animal import *

def Vet(animalsList):
    print("The animals we have are: ")
    for animal in animalsList:
        print(animal.name + " who is a " + animal.value + ".")
    

Bob = Cat("Bob", "brown", 5, 20, False, 20)
Bob.legs = 4
Bob.collar_color = "black"

Lily = Cat("Lily", "white", 6, 10, False, 20)
Lily.legs = 4
Lily.collar_color = "black"

Birdie = Bird("Birdie", "blue", 5, 20, False, 2)
Birdie.legs = 2
Birdie.wings = 2
Birdie.collar_color = "black"

Tweety = Bird("Tweety", "yellow", 5, 10, False, 1)
Tweety.legs = 2
Tweety.wings = 2
Tweety.collar_color = "black"

Animals = [Bob, Birdie, Lily, Tweety]

Vet(Animals)