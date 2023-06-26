import numpy as np

def selection_sort(array):
    n = len(array)

    for i in range(n):
        minimun_id = i
        for j in range(i + 1, n):
            if array[minimun_id] > array[j]:
                minimun_id = j

        temp = array[i]
        array[i] = array[minimun_id]
        array[minimun_id] = temp

    return array

print(selection_sort(np.array([15, 34, 8, 3])))