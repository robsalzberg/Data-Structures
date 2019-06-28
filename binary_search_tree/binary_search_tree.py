class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check if the new node's value is less than
        # Is there not a child? If not insert new node
        # Repeat the process ** Check if the new node is greater than or less than
        # Check if new node's value is greater than
        # Is there a child? If not insert new node
        # Repeat the process

        if value < self.value:
            if not self.left:                           # if new node value greater than the root
                self.left = BinarySearchTree(value)     # then child left value is equal to the BinarySearchTree's value
            else:
                self.left.insert(value)                 # else if less than insert new node value as child left value
        else:
            if not self.right:                          # if new node value less than the root
                self.right = BinarySearchTree(value)      # then child right value is equal to the BinarySearchTree's value
            else:
                self.right.insert(value)                # else if greater than insert new node value as child right value

    def contains(self, target):
        if self.value == target:                                    # if the target is the same as the self value return true
            return True                         
        branch = self.left if target < self.value else self.right   # set a new branch pointing to left if value is less than self value otherwise point it to the right
        if branch is None:                                          # if the branch points nowhere return false
            return False                                    
        return branch.contains(target)                              # otherwise return a recursive call on target

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)

        if self.right is None and self.left is None:
            return
        else:
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)
        return
