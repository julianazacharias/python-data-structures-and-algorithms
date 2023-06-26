import numpy as np

class Vertex:

  def __init__(self, label, target_distance):
    self.label = label
    self.visited = False
    self.target_distance = target_distance
    self.adjacent = []

  def add_adjacent(self, adjacent):
    self.adjacent.append(adjacent)

  def show_adjacent(self):
    for i in self.adjacent:
      print(i.vertex.label, i.cost)

class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost
    self.astar_distance = vertex.target_distance + self.cost

class Graph:
  arad = Vertex('Arad', 366)
  zerind = Vertex('Zerind', 374)
  oradea = Vertex('Oradea', 380)
  sibiu = Vertex('Sibiu', 253)
  timisoara = Vertex('Timisoara', 329)
  lugoj = Vertex('Lugoj', 244)
  mehadia = Vertex('Mehadia', 241)
  dobreta = Vertex('Dobreta', 242)
  craiova = Vertex('Craiova', 160)
  rimnicu = Vertex('Rimnicu', 193)
  fagaras = Vertex('Fagaras', 178)
  pitesti = Vertex('Pitesti', 98)
  bucharest = Vertex('Bucharest', 0)
  giurgiu = Vertex('Giurgiu', 77)

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

class SortedArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        # Change in data type
        self.values = np.empty(self.capacity, dtype=object)

    # Reference to vertex and comparison with distance A*
    def insert(self, adjacent):
        if self.last_position == self.capacity - 1:
            print('maximum capacity reached')
            return
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].astar_distance > adjacent.astar_distance:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = adjacent
        self.last_position += 1

    def print_search(self):
        if self.last_position == -1:
            print('The array is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i].vertex.label, ' - ',
                      self.values[i].cost, ' - ',
                      self.values[i].vertex.target_distance, ' - ',
                      self.values[i].astar_distance)

class AStar:
  def __init__(self, target):
    self.target = target
    self.found = False

  def search(self, current):
    print('----------')
    print('Current: {}'.format(current.label))
    current.visited = True

    if current == self.target:
      self.found = True
    else:
      sorted_array = SortedArray(len(current.adjacent))
      for adjacent in current.adjacent:
        if adjacent.vertex.visited == False:
          adjacent.vertex.visited = True
          sorted_array.insert(adjacent)
      sorted_array.print_search()

      if sorted_array.values[0] != None:
        self.search(sorted_array.values[0].vertex)

astar_search = AStar(graph.bucharest)
astar_search.search(graph.arad)