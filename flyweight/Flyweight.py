#
# Python Design Patterns: Flyweight
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Flyweight
# declares an interface through which flyweights can receive
# and act on extrinsic state
#
class Flyweight:
  def operation(self):
    pass
  
#
# UnsharedConcreteFlyweight
# not all subclasses need to be shared
#
class UnsharedConcreteFlyweight(Flyweight):
  def __init__(self, state):
    Flyweight.__init__(self)
    self._state = state
  
  def operation(self):
    print("Unshared Flyweight with state " + str(self._state))

#
# ConcreteFlyweight
# implements the Flyweight interface and adds storage
# for intrinsic state
#
class ConcreteFlyweight(Flyweight):
  def __init__(self, state):
    Flyweight.__init__(self)
    self._state = state
    
  def operation(self):
    print("Concrete Flyweight with state " + str(self._state))

#
# FlyweightFactory
# creates and manages flyweight objects and ensures
# that flyweights are shared properly
#
class FlyweightFactory:
  def __init__(self):
    self._flies = {}
  
  def getFlyweight(self, key):
    if (self._flies.get(key) is not None):
      return self._flies.get(key)
    
    self._flies[key] = ConcreteFlyweight(key)        
    return self._flies.get(key)


if __name__ == "__main__":
  factory = FlyweightFactory()

  factory.getFlyweight(1).operation()
  factory.getFlyweight(2).operation()
