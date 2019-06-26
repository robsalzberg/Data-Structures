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
                self.right = BinarySearchTree(value)    # then child right value is equal to the BinarySearchTree's value
            else:
                self.right.insert(value)                # else if greater than insert new node value as child right value

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
