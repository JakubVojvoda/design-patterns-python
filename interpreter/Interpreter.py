#
# Python Design Patterns: Interpreter
# Author: Jakub Vojvoda [github.com/JakubVojvoda]
# 2016
#
# Source code is licensed under MIT License
# (for more details see LICENSE)
# 

import sys

#
# Context
# contains information that's global to the interpreter
#
class Context:
  def __init__(self):
    self._vars = {}
  
  def set(self, var, value):
    self._vars[var] = value
  
  def get(self, exp):
    return self._vars[exp]

#
# Abstract Expression
# declares an abstract Interpret operation that is common to all nodes
# in the abstract syntax tree
#
class AbstractExpression:
  def interpret(self, context):
    return False

#
# Terminal Expression
# implements an Interpret operation associated with terminal symbols
# in the grammar (an instance is required for every terminal symbol
# in a sentence)
#
class TerminalExpression(AbstractExpression):
  def __init__(self, value):
    AbstractExpression.__init__(self)
    self._value = value
  
  def interpret(self, context):
    return context.get(self._value)

#
# Nonterminal Expression
# implements an Interpret operation for nonterminal symbols
# in the grammar (one such class is required for every rule in the grammar)
#
class NonterminalExpression(AbstractExpression):
  def __init__(self, expr_left, expr_right):
    self._lop = expr_left
    self._rop = expr_right

  def interpret(self, context):
    return self._lop.interpret(context) and self._rop.interpret(context)


# An example of very simple expression tree
# that corresponds to expression (A AND B)
if __name__ == "__main__":
  A = TerminalExpression("A")
  B = TerminalExpression("B")
  exp = NonterminalExpression(A, B)

  context = Context()
  context.set("A", True)
  context.set("B", True)

  print(str(context.get("A")) + " AND " + str(context.get("B")), end = "" )
  print(" = " + str(exp.interpret(context)))

  context.set("A", True)
  context.set("B", False)

  print(str(context.get("A")) + " AND " + str(context.get("B")), end = "" )
  print(" = " + str(exp.interpret(context)))
