"""
                    The Interface Segregation Principle (ISP)


  The content of a subclass clean from elements of no use to that subclass.
                             This has the final aim to keep our classes clean and minimise mistakes
"""

from abc import ABC, abstractmethod


""" 
  we create smaller role interfaces for each method.
      The respective classes would only use related interfaces
"""
class Django():

  @abstractmethod
  def django(self):
    pass

class Flask():

  @abstractmethod
  def flask(self):
    pass

class FastAPI():

  @abstractmethod
  def fastapi(self):
    pass


class BoostUP(Flask):

  def flask(self):
    print("Flask Implementations")

class SalonLet(Django):

  def django(self):
    print("Django Implementations")

class Project(Django,FastAPI):

  def django(self):
    print("Django Implementations")

  def fastapi(self):
    print("FastAPI Implementations")  



p = Project()
p.django()
p.fastapi()


# Example 2

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


