import numpy as np

class PriorityQueue:

    def __init__(self, capacity):
        self.capacity = capacity
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

        if self.num_elements == 0:
            self.values[self.num_elements] = value
            self.num_elements += 1
        else:
            x = self.num_elements - 1
            while x >= 0:
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                else:
                    break
                x -= 1
            self.values[x + 1] = value
            self.num_elements += 1

    def pop(self):
        if self.__empty_queue():
            print('Queue is empty')
            return

        value = self.values[self.num_elements - 1]
        self.num_elements -= 1
        return value

    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.num_elements - 1]

queue = PriorityQueue(5)
queue.push(30)
queue.push(50)
queue.push(10)
queue.push(40)
queue.push(20)
queue.pop()
queue.pop()
queue.pop()
queue.push(5)

print(queue.first())