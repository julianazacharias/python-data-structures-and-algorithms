import numpy as np

class Stack:
  def __init__(self, capacity):
    self.capacity = capacity
    self.top = -1
    # char array (b'(')
    self.values = np.chararray(self.capacity, unicode=True)

  def __full_Stack(self):
    if self.top == self.capacity - 1:
      return True
    else:
      return False

  # Public method
  def empty_stack(self):
    if self.top == -1:
      return True
    else:
      return False

  def stack_up(self, value):
    if self.__full_Stack():
      print('Stack is full')
    else:
      self.top += 1
      self.values[self.top] = value

  # Returns the popped element
  def unstack(self):
    if self.empty_stack():
      print('Stack is empty')
      return -1
    else:
      value = self.values[self.top]
      self.top -= 1
      return value

  def show_top(self):
    if self.top != -1:
      return self.values[self.top]
    else:
      return -1


# ------------------------- Testing with expression validation -------------------------

# c[d]
# a{b[c]d}e
# a{b(c]d}e
# a[b{c}d]e}
# a{b(c)

print("# --------- Testing with expression validation ---------")
print()

expression = str(input('Type an expression'))
stack = Stack(len(expression))

for i in range(len(expression)):
  ch = expression[i]
  if ch == '{' or ch == '[' or ch == '(':
    stack.stack_up(ch)
  elif ch == '}' or ch == ']' or ch == ')':
    if not stack.empty_stack():
      chx = str(stack.unstack())
      if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
        print('Error: ', ch, ' in position ', i)
        break
    else:
        print('Error: ', ch, ' in position ', i)
if not stack.empty_stack():
    print('Error!')