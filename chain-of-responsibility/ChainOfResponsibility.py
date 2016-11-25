#
# Python Design Patterns: Chain of Responsibility 
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Handler
# defines an interface for handling requests and
# optionally implements the successor link
#
class Handler:
  def __init__(self):
    self._successor = None  

  def setHandler(self, successor):
    self._successor = successor

  def handleRequest(self):
    if (self._successor is not None):
      self._successor.handleRequest();

#
# Concrete Handlers
# handle requests they are responsible for
#
class ConcreteHandler1(Handler):
  def __init__(self):
    Handler.__init__(self)
    self._can_handle = False  

  def handleRequest(self):
    if (self._can_handle):
      print( "Handled by Concrete Handler 1.")
    else:
      print("Cannot be handled by Handler 1.")
      super().handleRequest()

class ConcreteHandler2(Handler):
  def __init__(self):
    Handler.__init__(self)
    self._can_handle = True  

  def handleRequest(self):
    if (self._can_handle):
      print( "Handled by Concrete Handler 2.")
    else:
      print("Cannot be handled by Handler 2.")
      super().handleRequest()


if __name__ == "__main__":
  handler1 = ConcreteHandler1()
  handler2 = ConcreteHandler2()
  
  handler1.setHandler(handler2)
  handler1.handleRequest()
  