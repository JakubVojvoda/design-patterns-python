#
# Python Design Patterns: Facade
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Subsystems
# implement more complex subsystem functionality
# and have no knowledge of the facade
#
class SubsystemA:
  def suboperation(self):
    print("Subsystem A method")

class SubsystemB:
  def suboperation(self):
    print("Subsystem B method")

class SubsystemC:
  def suboperation(self):
    print("Subsystem C method")

#
# Facade
# delegates client requests to appropriate subsystem object
# and unified interface that is easier to use
#
class Facade:
  def __init__(self):
    self._subA = SubsystemA()
    self._subB = SubsystemB()
    self._subC = SubsystemC()

  def operation1(self):
    self._subA.suboperation()
    self._subB.suboperation()

  def operation2(self):
    self._subC.suboperation()


if __name__ == "__main__":
  facade = Facade()
  facade.operation1()
  facade.operation2()