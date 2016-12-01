#
# Python Design Patterns: Memento
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Memento
# stores internal state of the Originator object and protects
# against access by objects other than the originator
#
class Memento:
  def __init__(self, state):
    self._state = state   

  def setState(self, state):
    self._state = state;

  def getState(self):
    return self._state
  
#
# Originator
# creates a memento containing a snapshot of its current internal
# state and uses the memento to restore its internal state
#
class Originator:
  def __init__(self):
    self._state = 0
      
  def setState(self, state):
    print("Set state to " + str(state) + ".")
    self._state = state

  def getState(self):
    return self._state

  def setMemento(self, memento):
    self._state = memento.getState()

  def createMemento(self):
    return Memento(self._state)

#
# CareTaker
# is responsible for the memento's safe keeping
#
class CareTaker:
  def __init__(self, originator):
    self._originator = originator
    self._history = []

  def save(self):
    print("Save state.")
    self._history.append(self._originator.createMemento())

  def undo(self):
    print("Undo state.")
    self._originator.setMemento(self._history[-1])
    self._history.pop()


if __name__ == "__main__":
  originator = Originator()
  caretaker = CareTaker(originator)

  originator.setState(1)
  caretaker.save()

  originator.setState(2)
  caretaker.save()

  originator.setState(3)
  caretaker.undo()

  print("Actual state is " + str(originator.getState()) + ".")
