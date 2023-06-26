import numpy as np

class SortedArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def show(self):
        if self.last_position == -1:
            print('The array is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    # O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('It has reached the limit')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

    # O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1

    # O(log n)
    def binary_search(self, value):
        lower_limit = 0
        upper_limit = self.last_position

        while True:
            current_position = int((lower_limit + upper_limit) / 2)
            # If found it in the first attempt
            if self.values[current_position] == value:
                return current_position
            # If did not find it
            elif lower_limit > upper_limit:
                return -1
            # split limits
            else:
                # Lower limit
                if self.values[current_position] < value:
                    lower_limit = current_position + 1
                # Upper limit
                else:
                    upper_limit = current_position - 1

    # O(n)
    def excluir(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1

array = SortedArray(10)
array.insert(8)
array.insert(9)
array.insert(4)
array.insert(1)
array.insert(5)
array.insert(7)
array.insert(11)
array.insert(13)
array.insert(2)


array.show()

print("--------------------------")

array.binary_search(7)
array.binary_search(5)
array.binary_search(13)
array.binary_search(20)


array.show()