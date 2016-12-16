#
# Python Design Patterns: Visitor
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Visitor
# declares a Visit operation for each class of ConcreteElement
# in the object structure
#
class Visitor:
  def visitElementA(self, element):
    pass
  
  def visitElemeentB(self, element):
    pass
    
#
# Concrete Visitors
# implement each operation declared by Visitor, which implement
# a fragment of the algorithm defined for the corresponding class
# of object in the structure
#    
class ConcreteVisitor1(Visitor):
  def __init__(self):
    Visitor.__init__(self)  

  def visitElementA(self, concreteElementA):
    print("Concrete Visitor 1: Element A visited.")

  def visitElementB(self, concreteElementB):
    print("Concrete Visitor 1: Element B visited.")
  
class ConcreteVisitor2(Visitor):
  def __init__(self):
    Visitor.__init__(self)  
    
  def visitElementA(self, concreteElementA):
    print("Concrete Visitor 2: Element A visited.")

  def visitElementB(self, concreteElementB):
    print("Concrete Visitor 2: Element B visited.")

#
# Element
# defines an accept operation that takes a visitor as an argument
#
class Element:
  def accept(self, visitor):
    pass

#
# Concrete Elements
# implement an accept operation that takes a visitor as an argument
#
class ConcreteElementA(Element):
  def __init__(self):
    Element.__init__(self)  

  def accept(self, visitor):
    visitor.visitElementA(self)

class ConcreteElementB(Element):
  def __init__(self):
    Element.__init__(self)  
  
  def accept(self, visitor):
    visitor.visitElementB(self)
    

if __name__ == "__main__":
  elementA = ConcreteElementA()
  elementB = ConcreteElementB()
  
  visitor1 = ConcreteVisitor1()
  visitor2 = ConcreteVisitor2()
  
  elementA.accept(visitor1)
  elementA.accept(visitor2)
  
  elementB.accept(visitor1)
  elementB.accept(visitor2)
  