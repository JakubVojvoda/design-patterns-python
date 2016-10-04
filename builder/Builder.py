#
# Python Design Patterns: Builder
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Product
# the final object that will be created using Builder
#
class Product:
  def __init__(self):
    self._partA = ""
    self._partB = ""
    self._partC = ""

  def makeA(self, part):
    self._partA = part
        
  def makeB(self, part):
    self._partB = part
  
  def makeC(self, part):
    self._partC = part
  
  def get(self):
    return self._partA +" "+ self._partB +" "+ self._partC  

#
# Builder
# abstract interface for creating products
#
class Builder:
  def __init__(self):
    self._product = Product()
    
  def get(self):
    return self._product

  def buildPartA():
    pass
    
  def buildPartB():
    pass
  
  def buildPartC():
    pass

#
# Concrete Builders
# create real products and stores them in the composite structure
#
class ConcreteBuilderX(Builder):
  def __init__(self):
    Builder.__init__(self)

  def buildPartA(self):
    self._product.makeA("A-X")
  
  def buildPartB(self):
    self._product.makeB("B-X")
  
  def buildPartC(self):
    self._product.makeC("C-X")    

class ConcreteBuilderY(Builder):
  def __init__(self):
    Builder.__init__(self)
  
  def buildPartA(self):
    self._product.makeA("A-Y")
  
  def buildPartB(self):
    self._product.makeB("B-Y")
  
  def buildPartC(self):
    self._product.makeC("C-Y")    

#
# Director
# responsible for managing the correct sequence of object creation
#
class Director:
  def __init__(self):
    self._builder = None
  
  def set(self, builder):
    self._builder = builder  

  def get(self):
    return self._builder.get()
  
  def construct(self):
    self._builder.buildPartA()
    self._builder.buildPartB()
    self._builder.buildPartC()
      

if __name__ == "__main__":
  builderX = ConcreteBuilderX()
  builderY = ConcreteBuilderY()  
  
  director = Director()
  director.set(builderX)  
  director.construct()
  
  product1 = director.get()
  print("1st product parts: " + product1.get())
  
  director.set(builderY)  
  director.construct()
  
  product2 = director.get()
  print("2nd product parts: " + product2.get())
                                                                                        