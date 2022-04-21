from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes

    color = None
    Age = None
    Speed = None

    #Constructors
    def __init__(self):
        self.value = "Animal"

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
    
    def dies(self):
        return "I am dead RIP"

class Mammal(Animal):
    #Attributes

    legs = None

    #Constructors
    def __init__(self):
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

class Bird(Animal):
    
    # Attributes
    
    name = None
    wings = None
    legs = None
    
    def __init__(self):
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

class Cat(Mammal):
     #Attributes

    name = None
    collar_color = None

    #Constructors
    def __init__(self):
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