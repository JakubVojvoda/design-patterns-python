#
# Python Design Patterns: Composite
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Component
# defines an interface for all objects in the composition
# both the composite and the leaf nodes
#
class Component:
  def getChild(self, index):
    pass
  
  def add(self, component):
    pass
  
  def remove(self, index):
    pass
  
  def operation(self):
    pass

#
# Composite
# defines behavior of the components having children
# and store child components
#
class Composite(Component):
  def __init__(self):
    Component.__init__(self)
    self._children = []
  
  def getChild(self, index):
    return self._children[index]
  
  def add(self, component):
    self._children.append(component)   
  
  def remove(self, index):
    self._children.remove(index)
  
  def operation(self):
    for i in range(len(self._children)):
      self._children[i].operation()
      
#
# Leaf
# defines the behavior for the elements in the composition,
# it has no children
#
class Leaf(Component):
  def __init__(self, index):
    Component.__init__(self)
    self._idx = index
  
  def operation(self):
    print("Leaf " + str(self._idx) + " operation.")
      

if __name__ == "__main__":
  composite = Composite()
  
  for i in range(5):
    composite.add(Leaf(i))
  
  composite.operation()    