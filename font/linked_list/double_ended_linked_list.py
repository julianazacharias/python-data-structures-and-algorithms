class Node: 
  
  def __init__(self, value):
    self.value = value
    self.next = None

  def show_node(self):
    print(self.value)

class DoubleEndedLinkedList:

  def __init__(self):
    self.first = None
    self.last = None
  
  def __empty_list(self):
    return self.first == None

  def insert_start(self, value):
    new = Node(value)
    if self.__empty_list():
      self.last = new
    new.next = self.first
    self.first = new

  def insert_end(self, value):
    new = Node(value)
    if self.__empty_list():
      self.first = new
    else:
      self.last.next = new
    self.last = new

  def remove_start(self):
    if self.__empty_list():
      print('List is empty')
      return

    temp = self.first
    if self.first.next == None:
      self.last = None
    self.first = self.first.next
    return temp

  def show(self):
    if self.__empty_list():
      print('List is empty')
      return
    current = self.first
    while current != None:
      current.show_node()
      current = current.next

list = DoubleEndedLinkedList()

list.insert_start(1)
list.insert_start(2)
list.insert_start(3)
list.insert_start(4)
list.insert_start(5)

print("--------------------------------------")
list.show()

list.first, list.last

list.insert_end(1)
list.insert_end(2)
list.insert_end(3)

print("--------------------------------------")
list.show()

list.first, list.last

list.insert_start(0)
list.insert_end(4)

print("--------------------------------------")
list.show()

print("--------------------------------------")
list.remove_start()
list.show()
print("--------------------------------------")
