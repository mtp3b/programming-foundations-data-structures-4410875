#DOES NOT WORK. Refer to 06_05e
from collections import deque

def matching_parentheses(string):
  stack = deque(string)
  x = 0
  y = 0
  for char in stack:
    z = stack.pop()
    if z == ')':
      x = x + 1
    elif z == '(':
      y = y + 1
  
  if x == y:
    return True
  return False

print(matching_parentheses('hello(())'))
