#
# Python Design Patterns: Iterator
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Aggregate
# has a collection of objects and implements the method
# that returns an Iterator for its collection
#
class Aggregate:
  def __init__(self):
    self._list = []

  def __iter__(self):
    return Iterator(self._list)
  
  def get(self, index):
    return self._list[index]

  def set(self, l):
    self._list = l
  
#
# Iterator
# implements methods for traversing over elements and 
# is responsible for managing the current position of the iterator
#
class Iterator:
  def __init__(self, aggregate):
    self._list = aggregate
    self._size = len(aggregate)
    self._index = 0
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._index < self._size:
      pos = self._index
      self._index += 1
      return aggregate.get(pos)
    else:
      raise StopIteration()


if __name__ == "__main__": 
  aggregate = Aggregate()  
  aggregate.set([10,20,30,40,50])
  
  for value in list(aggregate):
    print("Item value: " + str(value))
  