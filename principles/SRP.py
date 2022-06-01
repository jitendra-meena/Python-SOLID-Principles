"""
  The Single-Responsibility Principle (SRP)
    
    a class should be responsible for only one functionality
"""

def data_count(list_):
    c=0
    for i in list_:
        c = c+i
    print(c)

def data_get(list_):
    for i in list_:
        print(i)

        
def data(list_):
    
    data_count(list_)
    data_get(list_)

data([1,2,3,4,5])