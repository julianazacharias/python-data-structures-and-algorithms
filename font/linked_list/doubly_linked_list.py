class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def show_node(self):
        print(self.value)

class DoublyLinkedLIst:

    def __init__(self):
        self.first = None
        self.last = None

    def __empty_list(self):
        return self.first == None

    def insert_start(self, value):
        new = Node(value)
        if self.__empty_list():
            self.last = new
        else:
            self.first.previous = new
        new.next = self.first
        self.first = new

    def insert_end(self, value):
        new = Node(value)
        if self.__empty_list():
            self.first = new
        else:
            self.last.next = new
            new.previous = self.last
        self.last = new

    def remove_start(self):
        temp = self.first
        if self.first.next == None:
            self.last = None
        else:
            self.first.next.previous = None
        self.first = self.first.next
        return temp

    def remove_end(self):
        temp = self.last
        if self.first.next == None:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        return temp

    def remove_position(self, value):
        current = self.first
        while current.value != value:
            current = current.next
            if current == None:
                return None
        if current == self.first:
            self.first = current.next
        else:
            current.previous.next = current.next

        if current == self.last:
            self.last = current.previous
        else:
            current.next.previous = current.previous
        return current

    def show_front(self):
        current = self.first
        while current != None:
            current.show_node()
            current = current.next

    def show_back(self):
        current = self.last
        while current != None:
            current.show_node()
            current = current.previous

list = DoublyLinkedLIst()

list.insert_start(1)
list.insert_start(2)
list.insert_end(3)
list.insert_end(4)

list.show_front()

list.remove_start()
list.remove_end()
list.remove_position(3)