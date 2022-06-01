""" 
   The Liskov Substitution Principle (LSP)

    Classes should be substitutable by instances of their subclasses. 
    
    Functions that use pointers or references to base classes must be able to
                use objects of derived classes without knowing it”

          [ IS-A Relationship ] 
"""


from abc import ABC, abstractmethod

class Bird(ABC):
   
    def __init__(self, name):
        self.name = name
   
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def do_sound(self) -> str:
        pass

class Crow(Bird):
   
    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def swim(self):
        raise NotImplementedError("Crows don't swim!")

    def do_sound(self) -> str:
        return "Caw"

class Duck(Bird):
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"