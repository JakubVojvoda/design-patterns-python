#
# Python Design Patterns: Observer
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys
   
#
# Observer
# defines an updating interface for objects that should be notified
# of changes in a subject
#
class Observer:
  def getState(self):
    pass
    
  def update(self, subject):
    pass
  
#
# Concrete Observer
# stores state of interest to ConcreteObserver objects and
# sends a notification to its observers when its state changes
#
class ConcreteObserver(Observer):
  def __init__(self, state):
    Observer.__init__(self)
    self._state = state
  
  def getState(self):
    return self._state
  
  def update(self, subject):
    self._state = subject.getState()
    print("Observer state updated.")
  
#
# Subject
# knows its observers and provides an interface for attaching
# and detaching observers
#
class Subject:
  def __init__(self):
    self._observers = []

  def attach(self, observer):
    self._observers.append(observer)

  def detach(self, index):
    self._observers.remove(index)

  def notify(self):
    for observer in self._observers:
      observer.update(self)

  def getState(self):
    pass
    
  def setState(self, state):
    pass

#
# Concrete Subject
# stores state that should stay consistent with the subject's
#
class ConcreteSubject(Subject):
  def __init__(self):
    Subject.__init__(self)
    self._state = 0
  
  def getState(self):
    return self._state

  def setState(self, state):
    self._state = state


if __name__ == "__main__":  
  observer1 = ConcreteObserver(1)
  observer2 = ConcreteObserver(2)

  print("Observer 1 state: " + str(observer1.getState()))
  print("Observer 2 state: " + str(observer2.getState()))

  subject = ConcreteSubject()
  subject.attach(observer1)
  subject.attach(observer2)

  subject.setState(10)
  subject.notify()

  print("Observer 1 state: " + str(observer1.getState()))
  print("Observer 2 state: " + str(observer2.getState()))
