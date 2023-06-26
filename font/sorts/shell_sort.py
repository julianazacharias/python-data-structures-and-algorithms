import numpy as np

def shell_sort(array):
    interval = len(array) // 2

    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

    return array


print(shell_sort(np.array([8, 5, 1, 4, 2, 3])))