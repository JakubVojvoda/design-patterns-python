#
# Python Design Patterns: State
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# State
# defines an interface for encapsulating the behavior associated
# with a particular state of the Context
#
class State:
  def handle(self):
    pass

#
# Concrete States
# each subclass implements a behavior associated with a state
# of the Context
#
class ConcreteStateA(State):
  def __init__(self):
    State.__init__(self)  
  
  def handle(self):
    print("State A handled.")

class ConcreteStateB(State):
  def __init__(self):
    State.__init__(self)  
  
  def handle(self):
    print("State B handled.")

#
# Context
# defines the interface of interest to clients
#
class Context:
  def __init__(self):
    self._state = State()
    
  def setState(self, state):
    self._state = state

  def request(self):
    self._state.handle()


if __name__ == "__main__":
  stateA = ConcreteStateA()
  stateB = ConcreteStateB()
  
  context = Context()
  
  context.setState(stateA)
  context.request()

  context.setState(stateB)
  context.request()
