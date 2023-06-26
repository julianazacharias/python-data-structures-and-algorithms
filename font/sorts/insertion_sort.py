import numpy as np

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        marker = array[i]

        j = i - 1
        while j >= 0 and marker < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marker

    return array


print(insertion_sort(np.array([15, 34, 8, 3])))