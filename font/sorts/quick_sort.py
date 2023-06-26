import numpy as np

def partition(array, start, end):
  pivot = array[end]
  i = start - 1

  for j in range(start, end):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i] # replacing --> In this way there is no need to use the var temp
  array[i + 1], array[end] = array[end], array[i + 1]
  return i + 1

def quick_sort(array, start, end):
  if start < end:
    position = partition(array, start, end)
    # Left
    quick_sort(array, start, position - 1)
    # Right
    quick_sort(array, position + 1, end)
  return array

array = np.array([38, 27, 43, 3, 9, 82, 10])

print(quick_sort(array, 0, len(array) - 1))
