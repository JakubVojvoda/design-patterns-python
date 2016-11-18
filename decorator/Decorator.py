#
# Python Design Patterns: Decorator
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Component
# defines an interface for objects that can have responsibilities
# added to them dynamically
#
class Component:
  def operation(self):
    pass
  
#
# Concrete Component
# defines an object to which additional responsibilities
# can be attached
#
class ConcreteComponent(Component):
  def __init__(self):
    Component.__init__(self)

  def operation(self):
    print("Concrete Component operation")

#
# Decorator
# maintains a reference to a Component object and defines an interface
# that conforms to Component's interface
#
class Decorator(Component):
  def __init__(self, component):
    Component.__init__(self)
    self._component = component

  def operation(self):
    self._component.operation()
  
#
# Concrete Decorators
# add responsibilities to the component (can extend the state
# of the component)
#
class ConcreteDecoratorA(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator A")

class ConcreteDecoratorB(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator B")


if __name__ == "__main__":
  component = ConcreteDecoratorA(
        ConcreteDecoratorB( ConcreteComponent() ) )
              
  component.operation()
