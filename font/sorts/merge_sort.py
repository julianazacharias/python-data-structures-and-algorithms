import numpy as np

def merge_sort(array):
    if len(array) > 1:
        division = len(array)//2
        left = array[:division].copy()
        right = array[division:].copy()

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # sort left right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # final sorting
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

#testing
print(merge_sort(np.array([38, 27, 43, 3, 9, 82, 10])))