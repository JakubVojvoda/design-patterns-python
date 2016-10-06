#
# Python Design Patterns: Prototype
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys
import copy

#
# Prototype
# declares an interface for cloning itself
#
class Prototype:
  def clone(self):
    pass
  
  def getType(self):
    pass

#
# Concrete Prototypes
# implement an operation for cloning itself
#
class ConcretePrototypeA(Prototype):
  def clone(self):
    return copy.deepcopy(self)
  
  def getType(self):
    return "type A"  

class ConcretePrototypeB(Prototype):
  def clone(self):
    return copy.deepcopy(self)
  
  def getType(self):
    return "type B"  

#
# Client
# creates a new object by asking a prototype to clone itself
#
class Client:
  def __init__(self):
    self._types = [ConcretePrototypeA(), ConcretePrototypeB()]
  
  def make(self, index):
    return self._types[index].clone()     


if __name__ == "__main__":
  client = Client()
  
  prototype = client.make(0)
  print(prototype.getType())
  
  prototype = client.make(1)
  print(prototype.getType())                                                                                         