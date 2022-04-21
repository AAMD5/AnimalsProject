from Animal import *

# Animal: name, color, age, speed, weight are global attributes
# Mammal (Cat, Bat, Budgie): legs
# Cat: collarcolor
# Bird: name, wings, legs
# 

# Creating a cat named Bob
# name, color, age, speed, isDead, weight
Bob = Cat("Bob", "brown", 5, 20, False, 20)
Bob.legs = 4
Bob.collar_color = "black"

print("My name is", Bob.name)
print(Bob.eat())
print(Bob.move())
print(Bob.breathe())
print(Bob.reproduce())
print(Bob.grow())
print(Bob.isDead, "I am not dead!")
print("\n")

# Creating a bat named Dracula
# name, color, age, speed, isDead, weight
Dracula = Bat("Dracula", "black", 5, 20, False, 10)
Dracula.legs = 4
Dracula.wings = 2

print("My name is", Dracula.name)
print(Dracula.eat())
print(Dracula.move())
print(Dracula.breathe())
print(Dracula.reproduce())
print(Dracula.grow())
print("I have", Dracula.wings, "wings")
print("Dracula can fly:")
print("It is", Dracula.flying(), "! I can fly!")
print("Dracula's wings are injured, can he fly?")
print(Dracula.landing())
print(Dracula.dead())
print("\n")

# Creating a mammal Platypus named Platypus
# name, color, age, speed, isDead, weight
Platpus = Platypus("Platypus", "white", 5, 20, False, 20)
Platpus.legs = 4

print("My name is", Platpus.name)
print(Platpus.eat())
print(Platpus.move())
print(Platpus.breathe())
print(Platpus.reproduce())
print(Platpus.grow())
print(Platpus.dead())
print("\n")

# Creating a bird named Birdie
# name, color, age, speed, isDead, weight
Birdie = Bird("Birdie", "blue", 5, 20, False, 2)
Birdie.legs = 4
Birdie.wings = 2
Birdie.collar_color = "black"

print("My name is", Birdie.name)
print(Birdie.eat())
print(Birdie.move())
print(Birdie.breathe())
print(Birdie.reproduce())
print("I have", Birdie.wings, "wings")
print("Birdie can fly:")
print("It is", Birdie.flying(), "! I can fly!")
print("Birdie's wings are injured, can he fly?")
print(Birdie.landing())
print(Birdie.grow())
print(Birdie.dead())