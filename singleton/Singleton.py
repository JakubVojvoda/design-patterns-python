#
# Python Design Patterns: Singleton
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Singleton
# has variable to hold one instance of the class and 
# method which gives us a way to instantiate the class
#
# reference: http://stackoverflow.com/questions/31875
#
class Singleton:
  def __init__(self, instance):
    self._instance = instance

  def get(self):
    try:
      return self._only
    except AttributeError:
      self._only = self._instance()
      return self._only

  def __call__(self):
    raise TypeError("...")

@Singleton
class Class:
  def tell(self):
    print("This is singleton.")
 

if __name__ == "__main__": 
  singleton = Class.get()
  singleton.tell()                                                                                       