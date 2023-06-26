import numpy as np

class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.num_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty_queue(self):
        return self.num_elements == 0

    def __full_queue(self):
        return self.num_elements == self.capacity

    def push(self, value):
        if self.__full_queue():
            print('Queue is full')
            return

        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.num_elements += 1

    def pop(self):
        if self.__empty_queue():
            print('Queue is already empty')
            return

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity:
            self.start = 0
        self.num_elements -= 1
        return temp

    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.start]

queue = CircularQueue(5)
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.pop()
queue.pop()
queue.push(6)
queue.push(7)

print(queue.first())