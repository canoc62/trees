class Tree():
    def __init__(val, parent=None):
        self.val = val
        self.size = 1
        self.left = None
        self.right = None
        self.parent = parent

    def __eq__(self, other):
        return self.val == other.val and self.right == other.right and self.left = other.left and self.parent = other.parent

    def __ne__(self, other):
        return self.__eq__(other) == False

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def lte(self, other):
        return self.val < other.val or self.__eq__(other)

    def gte(self, other):
        return self.val > other.val or self.__eq__(other)

    def max(self):
        if self.right is None:
            return self.val
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.val
        return self.left.min()

    def insert(self, val):
        self.size += 1

        if val < self.val:
            if self.left is None:
                self.left = Tree(val, self)
            else:
                return self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Tree(val, self)
            else:
                return self.left.insert(val)
            return None
        # handle duplicate value scenario with splice?

   def select(self, position):
       if self.left:
           left_sub_tree_size = self.left.size
       else:
           left_sub_tree_size = 0

        if position == left_subtree_size + 1:
            return tree.left.val
        elif position < left_sub_tree_size + 1:
            return self.left(position)
        else:
            return self.right(position - left_sub_tree_size + 1)
            
