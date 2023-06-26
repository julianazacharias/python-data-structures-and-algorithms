class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def show_node(self):
    print(self.value)

class LinkedList:
  def __init__(self):
    self.first = None

  def insert_start(self, value):
    new = Node(value)
    new.next = self.first
    self.first = new

  def show(self):
    if self.first == None:
      print('List is empty')
      return None

    current = self.first
    while current != None:
      current.show_node()
      current = current.next

  def search(self, value):
    if self.first == None:
      print('List is empty')
      return None

    current = self.first
    while current.value != value:
      if current.next == None:
        return None
      else:
        current = current.next
    return current

  def remove_start(self):
    if self.first == None:
      print('List is empty')
      return None

    temp = self.first
    self.first = self.first.next
    return temp

  def remove_position(self, value):
    if self.first == None:
      print('List is empty')
      return None

    current = self.first
    previous = self.first
    while current.value != value:
      if current.next == None:
        return None
      else:
        previous = current
        current = current.next

    if current == self.first:
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

list = LinkedList()

list.insert_start(1)
list.insert_start(2)
list.insert_start(3)
list.insert_start(4)
list.insert_start(5)

search = list.search(3)

list.show()

list.remove_start()
list.remove_position(4)
list.remove_position(2)