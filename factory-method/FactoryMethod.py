#
# Python Design Patterns: Factory Method
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Product
# products implement the same interface so that the classes 
# can refer to the interface not the concrete product
#
class Product:
  def getName(self):
    pass

#
# Concrete Products
# define product to be created
#
class ConcreteProductA(Product):
  def getName(self):
    return "type A"

class ConcreteProductB(Product):
  def getName(self):
    return "type B"

#
# Creator
# contains the implementation for all of the methods
# to manipulate products except for the factory method
#
class Creator:
  def createProductA(self):
    pass
    
  def createProductB(self):
    pass

#
# Concrete Creator
# implements factory method that is responsible for creating
# one or more concrete products ie. it is class that has
# the knowledge of how to create the products
#
class ConcreteCreator(Creator):
  def createProductA(self):
    return ConcreteProductA()
  
  def createProductB(self):
    return ConcreteProductB()
  
  
if __name__ == "__main__":
  creator = ConcreteCreator()
  
  p1 = creator.createProductA()
  print("Product: " + p1.getName())
  
  p2 = creator.createProductB()
  print("Product: " + p2.getName())
