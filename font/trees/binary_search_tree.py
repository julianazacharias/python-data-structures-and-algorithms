
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def show_node(self):
    print(self.value)

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.connections = []

  def insert(self, value):
    new = Node(value)
    # Se a árvore estiver vazia
    if self.root == None:
      self.root = new
    else:
      current = self.root
      while True:
        parent = current
        # Left
        if value < current.value:
          current = current.left
          if current == None:
            parent.left = new
            self.connections.append(str(parent.value) + '->' + str(new.value))
            return
        # Right
        else:
          current = current.right
          if current == None:
            parent.right = new
            self.connections.append(str(parent.value) + '->' + str(new.value))
            return 

  def search(self, value):
    current = self.root
    while current.value != value:
      if value < current.value:
        current = current.left
      else:
        current = current.right
      if current == None:
        return None
    return current

  # Root, left, right
  def pre_order(self, node):
    if node != None:
      print(node.value)
      self.pre_order(node.left)
      self.pre_order(node.right)

  # Left, root, right
  def in_order(self, node):
    if node != None:
      self.in_order(node.left)
      print(node.value)
      self.in_order(node.right)

  # Left, right, root
  def post_order(self, node):
    if node != None:
      self.post_order(node.left)
      self.post_order(node.right)
      print(node.value)

  def excluir(self, value):
    if self.root == None:
      print('A árvore está vazia')
      return
    
    # Find the node
    current = self.root
    parent = self.root
    e_left = True
    while current.value != value:
      parent = current
      # Left
      if value < current.value:
        e_left = True
        current = current.left
      # Right
      else:
        e_left = False
        current = current.right
      if current == None:
        return False
    
    # Node to be deleted is a leaf
    if current.left == None and current.right == None:
      if current == self.root:
        self.root = None
      elif e_left == True:
        
        self.connections.remove(str(parent.value) + '->' + str(current.value))
        
        parent.left = None
      else:
        
        self.connections.remove(str(parent.value) + '->' + str(current.value))
        
        parent.right = None

    # Node to be deleted does not have a child on the right
    elif current.right == None:
      
      self.connections.remove(str(parent.value) + '->' + str(current.value))
      self.connections.remove(str(current.value) + '->' + str(current.left.value))
      
      if current == self.root:
        self.root = current.left

        self.connections.append(str(root.value) + '->' + str(current.left.value))

      elif e_left == True:
        parent.left = current.left

        self.connections.append(str(parent.value) + '->' + str(current.left.value))

      else:
        parent.right = current.left

        self.connections.append(str(parent.value) + '->' + str(current.left.value))

    # Node to be deleted does not have a child on the left
    elif current.left == None:

      self.connections.remove(str(parent.value) + '->' + str(current.value))
      self.connections.remove(str(current.value) + '->' + str(current.right.value))

      if current == self.root:

        self.connections.append(str(root.value) + '->' + str(current.right.value))

        self.root = current.right
      elif e_left == True:

        self.connections.append(str(parent.value) + '->' + str(current.right.value))

        parent.left = current.right
      else:

        self.connections.append(str(parent.value) + '->' + str(current.right.value))

        parent.right = current.right
    
    # The node has 2 childs
    else:
      sucessor = self.get_successor(current)

      self.connections.remove(str(parent.value) + '->' + str(current.value))
      self.connections.remove(str(current.right.value) + '->' + str(sucessor.value))
      self.connections.remove(str(current.value) + '->' + str(current.left.value))
      self.connections.remove(str(current.value) + '->' + str(current.right.value))

      if current == self.root:

        self.connections.append(str(root.value) + '->' + str(sucessor.value))     
        
        self.root = sucessor

      elif e_left == True:

        self.connections.append(str(parent.value) + '->' + str(sucessor.value))

        parent.left = sucessor

      else:

        self.connections.append(str(parent.value) + '->' + str(sucessor.value))

        parent.right = sucessor
      
      self.connections.append(str(sucessor.value) + '->' + str(current.left.value))
      self.connections.append(str(sucessor.value) + '->' + str(current.right.value))
      
      sucessor.left = current.left

    return True
  
  def get_successor(self, node):
    successor_parent = node
    successor = node
    current = node.right
    while current != None:
      successor_parent = successor
      successor = current
      current = current.left
    if successor != node.right:
      successor_parent.left = successor.right
      successor.right = node.right
    return successor
  
tree = BinarySearchTree()

tree.insert(53)
tree.insert(30)
tree.insert(14)
tree.insert(39)
tree.insert(9)
tree.insert(23)
tree.insert(34)
tree.insert(49)
tree.insert(72)
tree.insert(61)
tree.insert(84)
tree.insert(79)

print(tree.root.left.value)

print(tree.connections)

# tree.connections.remove('14->9')

print(tree.get_successor(tree.root).value)