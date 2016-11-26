#
# Python Design Patterns: Command
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Receiver
# knows how to perform the operations associated 
# with carrying out a request
#
class Receiver:
  def action(self):
    print("Receiver: execute action.")

#
# Command
# declares an interface for all commands
#
class Command:
  def execute(self):
    pass

#
# Concrete Command
# implements execute by invoking the corresponding 
# operation(s) on Receiver 
#
class ConcreteCommand(Command):
  def __init__(self, receiver):
    self._receiver = receiver

  def execute(self):
    self._receiver.action()

#
# Invoker
# asks the command to carry out the request
#
class Invoker:
  def __init__(self):
    self._command = None  
  
  def set(self, command):
    self._command = command

  def confirm(self):
    if (self._command is not None):
      self._command.execute()


if __name__ == "__main__":
  receiver = Receiver()
  command = ConcreteCommand(receiver)

  invoker = Invoker()
  invoker.set(command)
  invoker.confirm()
