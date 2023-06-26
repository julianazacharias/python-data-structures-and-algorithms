import sys
import numpy as np


vertexes = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
vertexes_inv = {0: 'A', 1: 'B', 2:'C', 3:'D', 4:'E', 5: 'F'}

edges = np.zeros([len(vertexes), len(vertexes)], dtype=int)
edges[vertexes['A'],[vertexes['B']]] = 2
edges[vertexes['A'],[vertexes['C']]] = 1
edges[vertexes['B'],[vertexes['D']]] = 1
edges[vertexes['C'],[vertexes['D']]] = 3
edges[vertexes['C'],[vertexes['E']]] = 4
edges[vertexes['D'],[vertexes['F']]] = 2
edges[vertexes['E'],[vertexes['F']]] = 2

class Dijkstra:
  def __init__(self, vertices, edges, start):
    self.size = len(vertices)
    self.vertices = vertices
    self.graphs = edges
    self.start = start

  def show_solution(self, distances):
    print('Shortest distances from {} to all others'.format(self.vertices[self.start]))
    for vertex in range(self.size):
      print(self.vertices[vertex], distances[vertex])

  def minnimun_index(self, distance, visited):
    minnimun = sys.maxsize
    for vertex in range(self.size):
      if distance[vertex] < minnimun and visited[vertex] == False:
        minnimun = distance[vertex]
        minimum_index = vertex
    return minimum_index

  def dijkstra(self):
    distance = [sys.maxsize] * self.size
    distance[self.start] = 0
    visited = [False] * self.size

    for _ in range(self.size):
      minimum_index = self.minnimun_index(distance, visited)
      visited[minimum_index] = True
      for vertex in range(self.size):
        if self.graphs[minimum_index][vertex] > 0 and visited[vertex] == False \
            and distance[vertex] > distance[minimum_index] + self.graphs[minimum_index][vertex]:
          distance[vertex] = distance[minimum_index] + self.graphs[minimum_index][vertex]

    self.show_solution(distance)

dijkstra = Dijkstra(vertexes_inv, edges, vertexes['A'])
dijkstra.dijkstra()