import numpy as np

class UnsortedArray:
  def __init__(self, capacity):
    self.capacity = capacity
    self.last_position = -1
    self.values = np.empty(self.capacity, dtype=int)

  def show(self):
    if self.last_position == -1:
      print('The array is empty')
    else:
      for i in range(self.last_position + 1):
        print(i, ' - ', self.values[i])
  
  def insert(self, value):
    if self.last_position == self.capacity - 1:
      print('It has reached the limit')
    else:
      self.last_position += 1
      self.values[self.last_position] = value

  def search(self, value):
    for i in range(self.last_position + 1):
      if value == self.values[i]:
        return i
    return -1

  def remove(self, value):
    position = self.search(value);
    if position == -1:
      return -1
    else:
      for i in range(position, self.last_position):
        self.values[i] = self.values[i + 1]
      
      self.last_position -= 1
      
      
array = UnsortedArray(10)

array.insert(3)
array.insert(2)
array.insert(4)
array.insert(5)
array.insert(6)
array.insert(1)

array.show()

array.search(5)

array.search(9)

array.remove(5)