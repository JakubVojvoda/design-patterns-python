#
# Python Design Patterns: Proxy
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Subject
# defines the common interface for RealSubject and Proxy
# so that a Proxy can be used anywhere a RealSubject is expected
#
class Subject:
  def request(self):
    pass

#
# Real Subject
# defines the real object that the proxy represents
#
class RealSubject(Subject):
  def __init__(self):
    Subject.__init__(self)  
    
  def request(self):
    print("Real Subject request.")

#
# Proxy
# maintains a reference that lets the proxy access the real subject
#
class Proxy(Subject):
  def __init__(self):
    Subject.__init__(self)
    self._subject = RealSubject()
    
  def request(self):
    self._subject.request()


if __name__ == "__main__":
  proxy = Proxy()
  proxy.request()
  