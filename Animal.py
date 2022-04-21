from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes

    name = None
    color = None
    age = None
    speed = None
    isDead = False
    weight = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        self.value = "Animal"
        self.name = name
        self.color = color
        self.age = age
        self.speed = speed
        self.isDead = isDead
        self.weight = weight

    #Methods
    @abstractmethod # so these are methods that will be defined later
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def breathe(self):
        pass

    def sleep(self):
        return "I am sleeping"

    def type(self):
        return self.value
    
    def grow(self):
        return "I am growing"
    
    def dead(self):
        self.isDead = True
        return self.isDead
    

class Mammal(Animal):
    #Attributes

    legs = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Mammal"

    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def breathe(self):
        pass    
    
    def reproduce(self):
        return "I give birth"

    def type(self):
        return self.value
    

class Cat(Mammal):
     #Attributes

    collar_color = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Cat"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat mice"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
    
class Bat(Mammal):
     #Attributes

    isFlying = False

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bat"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat meat"
    
    def move(self):
        return "I fly"
    
    def breathe(self):
        return "I breathe through my nose"
    
    def flying(self):
        self.isFlying = True
        return self.isFlying
    
    def landing(self):
        self.isFlying = False
        return self.isFlying
    
    
class Platypus(Mammal):
     #Attributes


    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Budgie"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat plants"
    
    def reproduce(self):
        return "I lay eggs"
    
    def move(self):
        return "I am amphibious"
    
    def breathe(self):
        return "I breathe through my nose"
    

class Bird(Animal):
    
    #Attributes
    
    wings = None
    legs = None
    isFlying = False
    
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bird"
        
    #Methods
    
    def reproduce(self):
        return "I lay eggs"
    
    def move(self):
        return "I fly, walk or run"
    
    def breathe(self):
        return "I breathe through my peak"   
    
    def type(self):
        return self.value
        
    def eat(self):
        return "I eat worms"
    
    def flying(self):
        self.isFlying = True
        return self.isFlying
    
    def landing(self):
        self.isFlying = False
        return self.isFlying