"""

  The Open-Closed Principle (OCP)

    classes should be open for extension, but closed for modification

"""


from abc import ABC, abstractmethod

class Operation(ABC):
    
    @abstractmethod
    def operation():
        pass

class Data_get(Operation):
    
    def operation(list_):
        for data in list_:
            print(data)

class Data_count(Operation):
    
    def operation(list_):
        c =0
        for data in list_:
            c = c+data
        print(c)

class Main():
    
    @abstractmethod
    def get_operations(list_):
        for orp in Operation.__subclasses__():
            orp.operation(list_)
       

Main.get_operations([1,2,3,4,5]) 
