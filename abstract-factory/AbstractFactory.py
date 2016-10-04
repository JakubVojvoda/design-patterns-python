#
# Python Design Patterns: Abstract Factory
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Product A
# products implement the same interface so that the classes can refer
# to the interface not the concrete product
#
class ProductA:
  def getName(self):
    pass

#
# ConcreteProductAX and ConcreteProductAY
# define objects to be created by concrete factory
#
class ConcreteProductAX(ProductA):
  def getName(self):
    return "A-X"

class ConcreteProductAY(ProductA):
  def getName(self):
    return "A-Y"

#
# Product B
# same as Product A, Product B declares interface for concrete products
# where each can produce an entire set of products
#
class ProductB:
  def getName(self):
    pass

#
# ConcreteProductBX and ConcreteProductBY
# same as previous concrete product classes
#
class ConcreteProductBX(ProductB):
  def getName(self):
    return "B-X"

class ConcreteProductBY(ProductB):
  def getName(self):
    return "B-Y"

#
# Abstract Factory
# provides an interface for creating a family of products
#
class AbstractFactory:
  def createProductA(self):
    pass
    
  def createProductB(self):
    pass
    
#
# Concrete Factories
# each concrete factory create a family of products and 
# client uses one of these factories
#
class ConcreteFactoryX(AbstractFactory):
  def createProductA(self):
    return ConcreteProductAX()
  
  def createProductB(self):
    return ConcreteProductBX()
     
class ConcreteFactoryY(AbstractFactory):
  def createProductA(self):
    return ConcreteProductAY()
  
  def createProductB(self):
    return ConcreteProductBY()

  
if __name__ == "__main__":
  factoryX = ConcreteFactoryX()
  factoryY = ConcreteFactoryY()
  
  p1 = factoryX.createProductA()
  print("Product: " + p1.getName())
  
  p2 = factoryY.createProductA()
  print("Product: " + p2.getName())
  
  
  
