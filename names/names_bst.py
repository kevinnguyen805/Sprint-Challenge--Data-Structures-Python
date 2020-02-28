class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # >= because you must account for a node value that is equal to the given insert value (not just smaller/bigger node values) """
    def insert(self, value):
        # checking to see if we can insert value at root (if root doesn't have a value yet)
        if value < self.value: 
            if self.left == None: 
                self.left = BinarySearchTree(value)
            else: 
                return self.left.insert(value)
        elif value >= self.value: 
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # Mistake here was not accounting for if the left/right node does not exist - explicitly returning False if it doesn't 
        # remember to use RETURN for recursive calls 
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False 
            else: 
                return self.left.contains(target)