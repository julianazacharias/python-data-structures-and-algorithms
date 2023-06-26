#DFS and BFS search

import numpy as np

class Vertex:
  def __init__(self, label):
    self.label = label
    self.visited = False
    self.adjacents = []

  def add_adjacent(self, adjacent):
    self.adjacents.append(adjacent)

  def show_adjacents(self):
    for i in self.adjacents:
      print(i.vertex.label, i.cost)

class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost

class Graph:
  arad = Vertex('Arad')
  zerind = Vertex('Zerind')
  oradea = Vertex('Oradea')
  sibiu = Vertex('Sibiu')
  timisoara = Vertex('Timisoara')
  lugoj = Vertex('Lugoj')
  mehadia = Vertex('Mehadia')
  dobreta = Vertex('Dobreta')
  craiova = Vertex('Craiova')
  rimnicu = Vertex('Rimnicu')
  fagaras = Vertex('Fagaras')
  pitesti = Vertex('Pitesti')
  bucharest = Vertex('Bucharest')
  giurgiu = Vertex('Giurgiu')

  arad.add_adjacent(Adjacent(zerind, 75))
  arad.add_adjacent(Adjacent(sibiu, 140))
  arad.add_adjacent(Adjacent(timisoara, 118))

  zerind.add_adjacent(Adjacent(arad, 75))
  zerind.add_adjacent(Adjacent(oradea, 71))

  oradea.add_adjacent(Adjacent(zerind, 71))
  oradea.add_adjacent(Adjacent(sibiu, 151))

  sibiu.add_adjacent(Adjacent(oradea, 151))
  sibiu.add_adjacent(Adjacent(arad, 140))
  sibiu.add_adjacent(Adjacent(fagaras, 99))
  sibiu.add_adjacent(Adjacent(rimnicu, 80))

  timisoara.add_adjacent(Adjacent(arad, 118))
  timisoara.add_adjacent(Adjacent(lugoj, 111))

  lugoj.add_adjacent(Adjacent(timisoara, 111))
  lugoj.add_adjacent(Adjacent(mehadia, 70))

  mehadia.add_adjacent(Adjacent(lugoj, 70))
  mehadia.add_adjacent(Adjacent(dobreta, 75))

  dobreta.add_adjacent(Adjacent(mehadia, 75))
  dobreta.add_adjacent(Adjacent(craiova, 120))

  craiova.add_adjacent(Adjacent(dobreta, 120))
  craiova.add_adjacent(Adjacent(pitesti, 138))
  craiova.add_adjacent(Adjacent(rimnicu, 146))

  rimnicu.add_adjacent(Adjacent(craiova, 146))
  rimnicu.add_adjacent(Adjacent(sibiu, 80))
  rimnicu.add_adjacent(Adjacent(pitesti, 97))

  fagaras.add_adjacent(Adjacent(sibiu, 99))
  fagaras.add_adjacent(Adjacent(bucharest, 211))

  pitesti.add_adjacent(Adjacent(rimnicu, 97))
  pitesti.add_adjacent(Adjacent(craiova, 138))
  pitesti.add_adjacent(Adjacent(bucharest, 101))

  bucharest.add_adjacent(Adjacent(fagaras, 211))
  bucharest.add_adjacent(Adjacent(pitesti, 101))
  bucharest.add_adjacent(Adjacent(giurgiu, 90))

graph = Graph()

class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.num_elements = 0

        # Change in data type
        self.values = np.empty(self.capacity, dtype=object)

    def __empty_queue(self):
        return self.num_elements == 0

    def __full_queue(self):
        return self.num_elements == self.capacity

    def push(self, value):
        if self.__full_queue():
            print('The queue is full')
            return

        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.num_elements += 1

    def pop(self):
        if self.__empty_queue():
            print('The queue is empty')
            return

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity - 1:
            self.start = 0
        self.num_elements -= 1
        return temp

    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.start]

class Stack:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__top = -1

    # Changing the array type
    self.__values = np.empty(self.__capacity, dtype=object)

  def __full_stack(self):
    if self.__top == self.__capacity - 1:
      return True
    else:
      return False

  def __empty_stack(self):
    if self.__top == -1:
      return True
    else:
      return False

  def stack_up(self, value):
    if self.__full_stack():
      print('The stack is full')
    else:
      self.__top += 1
      self.__values[self.__top] = value

  def unstack(self):
   # Return the popped element
    if self.__empty_stack():
      print('The stack is empty')
      return None
    else:
      temp = self.__values[self.__top]
      self.__top -= 1
      return temp

  def see_top(self):
    if self.__top != -1:
      return self.__values[self.__top]
    else:
      return -1

class DeepFirstSearch:
  def __init__(self, start):
    self.start = start
    self.start.visited = True
    self.stack = Stack(20)
    self.stack.stack_up(start)

  def search(self):
    top = self.stack.see_top()
    print('Top: {}'.format(top.label))
    for adjacent in top.adjacents:
      print('Top is {}. {} has been visited? {}'.format(top.label, adjacent.vertex.label, adjacent.vertex.visited))
      if adjacent.vertex.visited == False:
        adjacent.vertex.visited = True
        self.stack.stack_up(adjacent.vertex)
        print('Piled up {}'.format(adjacent.vertex.label))
        self.search()
    print('Unstacked: {}'.format(self.stack.unstack().label))
    print()

class BreadthFirstSearch:
  def __init__(self, start):
    self.start = start
    self.start.visited = True
    self.queue = CircularQueue(20)
    self.queue.push(start)

  def search(self):
    first = self.queue.first()
    print('-------')
    print('First in queue: {}'.format(first.label))
    temp = self.queue.pop()
    print('Dequeued: {}'.format(temp.label))
    for adjacent in first.adjacents:
      print('First was {}. {} has been visited? {}'.format(temp.label, adjacent.vertex.label, adjacent.vertex.visited))
      if adjacent.vertex.visited == False:
        adjacent.vertex.visited = True
        self.queue.push(adjacent.vertex)
        print('Queued: {}'.format(adjacent.vertex.label))
    if self.queue.num_elements > 0:
      self.search()

bfs = BreadthFirstSearch(graph.arad)
bfs.search()