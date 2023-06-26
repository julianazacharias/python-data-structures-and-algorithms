import numpy as np

class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.num_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __full_deque(self):
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)

    def __empty_deque(self):
        return self.start == -1

    def insert_start(self, value):
        if self.__full_deque():
            print('Deque is full')
            return

        # If is empty
        if self.start == -1:
            self.start = 0
            self.end = 0
        # Start in the first position
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -= 1

        self.values[self.start] = value

    def insert_end(self, value):
        if self.__full_deque():
            print('Deque is full')
            return

        # If is empty
        if self.start == -1:
            self.start = 0
            self.end = 0
        # End if is in the last position
        elif self.end == self.capacity - 1:
            self.end = 0
        else:
            self.end += 1

        self.values[self.end] = value

    def remove_start(self):
        if self.__empty_deque():
            print('Deque is already empty')
            return

        # Has only 1 element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            # Back to former position
            if self.start == self.capacity - 1:
                self.start = 0
            else:
                # Increment start to remove current start
                self.start += 1

    def remove_end(self):
        if self.__empty_deque():
            print('Deque is already empty')
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == 0:
            self.end = self.capacity - 1
        else:
            self.end -= 1

    def get_start(self):
        if self.__empty_deque():
            print('Deque is already empty')
            return

        return self.values[self.start]

    def get_end(self):
        if self.__empty_deque() or self.end < 0:
            print('Deque is already empty')
            return

        return self.values[self.end]

deque = Deque(5)
deque.insert_end(5)
deque.insert_end(10)
deque.insert_start(3)
deque.insert_start(2)
deque.insert_end(11)

deque.insert_start(43)

print(deque.get_start())
print(deque.get_end())

deque.remove_start()
deque.remove_end()

print("-------------")
print(deque.get_start())
print(deque.get_end())