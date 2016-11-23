#
# Python Design Patterns: Adapter
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Target
# defines specific interface that Client uses
#
class Target:
  def request(self):
    pass  

#
# Adaptee
# all requests get delegated to the Adaptee which defines
# an existing interface that needs adapting
#
class Adaptee:
  def specificRequest(self):
    print("Specific request")

#
# Adapter
# implements the Target interface and lets the Adaptee respond
# to request on a Target by extending both classes
# ie adapts the interface of Adaptee to the Target interface
#
class Adapter(Target, Adaptee):
  def __init__(self):
    Adaptee.__init__(self)
    Target.__init__(self)  
  
  def request(self):
    return self.specificRequest()  


if __name__ == "__main__":
  t = Adapter()
  t.request()
