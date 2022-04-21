from Animal import *

# Animal: name, color, age, speed, weight are global attributes
# Mammal (Cat, Bat, Budgie): legs
# Cat: collarcolor
# Bird: name, wings, legs
# 

# Creating a cat named Bob

Bob = Cat()
Bob.name = "Bob"
Bob.age = 5
Bob.legs = 4
Bob.speed = 20
Bob.collar_color = "black"
Bob.weight = 20

print("My name is", Bob.name)
print(Bob.eat())
print(Bob.move())
print(Bob.breathe())
print(Bob.reproduce())
print(Bob.grow())
print(Bob.isDead, "I am not dead!")
print("\n")

# Creating a bat named Dracula

Dracula = Bat()
Dracula.name = "Dracula"
Dracula.age = 5
Dracula.legs = 4
Dracula.wings = 2
Dracula.speed = 20
Dracula.weight = 10

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

Platypus = Platypus()
Platypus.name = "Platypus"
Platypus.age = 5
Platypus.legs = 4
Platypus.speed = 20
Platypus.weight = 20

print("My name is", Platypus.name)
print(Platypus.eat())
print(Platypus.move())
print(Platypus.breathe())
print(Platypus.reproduce())
print(Platypus.grow())
print(Platypus.dead())
print("\n")

# Creating a bird named Birdie

Birdie = Bird()
Birdie.name = "Birdie"
Birdie.age = 5
Birdie.legs = 4
Birdie.speed = 20
Birdie.wings = 2
Birdie.collar_color = "black"
Birdie.weight = 2

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

