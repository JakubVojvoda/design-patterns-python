#
# Python Design Patterns: Bridge
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Implementor
# defines the interface for implementation classes
#
class Implementor:
  def action(self):
    pass

#
# Concrete Implementors
# implement the Implementor interface and define concrete implementations
#
class ConcreteImplementorA(Implementor):
  def action(self):
    print("Concrete Implementor A")

class ConcreteImplementorB(Implementor):
  def action(self):
    print("Concrete Implementor B")

#
# Bridge
# decouple an abstraction from its implementation
#
class Bridge:
  def __init__(self, implementation):
    self._implementor = implementation
  
  def operation(self):
    self._implementor.action()


if __name__ == "__main__":
  bridge = Bridge(ConcreteImplementorA())
  bridge.operation()
  
  bridge = Bridge(ConcreteImplementorB())
  bridge.operation()
