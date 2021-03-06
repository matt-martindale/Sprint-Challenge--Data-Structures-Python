class NameNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = NameNode(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = NameNode(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    elif target >= self.value:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def in_order_print(self):
    if self.left:
      self.left.in_order_print()
    print(self.value)
    if self.right:
      self.right.in_order_print()
    