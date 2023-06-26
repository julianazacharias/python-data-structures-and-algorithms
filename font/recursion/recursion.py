def recursion(i):
  print('Recursion')
  i += 1
  if i == 5:
    return
  else:
    recursion(i)

recursion(0)


def sum(n):
  if n == 0:
    return 0

  return n + sum(n - 1)

print(sum(10))