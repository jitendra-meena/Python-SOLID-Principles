"""
  The Interface Segregation Principle (ISP)


  the content of a subclass clean from elements of no use to that subclass.
                             This has the final aim to keep our classes clean and minimise mistakes
"""


from abc import ABC, abstractmethod

class Walker(ABC):
  
  @abstractmethod
  def walk() -> bool:
    return print("Can Walk") 

class Swimmer(ABC):
  
  @abstractmethod
  def swim() -> bool:
    return print("Can Swim") 

class Human(Walker, Swimmer):

  def walk():
    return print("Humans can walk") 
  
  def swim():
    return print("Humans can swim") 

class Whale(Swimmer):
  
  def swim():
    return print("Whales can swim") 


Human.walk()
Human.swim()
Whale.swim()


