# AVL Tree: An AVL tree is a self-balancing tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_avl.py.

# IMPORTANT: For this implementation, starter code is provided.
# Do not modify the code provided 

# Name: Abbey Hankins
# Collaborators:
# Time spent:


class AVLTree:

    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.height = 0
        self.balance_factor = 0
        self.key = key
        
    def insert(self, node_to_insert):
        # A new node whose key is <= parent key becomes the left child
        if node_to_insert.key <= self.key:
            if not self._has_left_child():
                self.left = node_to_insert
            else:
                self.left.insert(node_to_insert)
        else:
            if not self._has_right_child():
                self.right = node_to_insert
            else:
                self.right.insert(node_to_insert)
        # The height of each node is equal to the height of its largest child + 1
        self.height = self._max_of_child_heights() + 1
        self.balance_factor = self._rebalance()



            
    # Here are some helper functions you may want to create
    # Right rotate around self
    def _right_rotate(self):
        pass
    
    # Left rotate around self
    def _left_rotate(self):
        pass
    
    # Return the largest height of self's children 
    def _max_of_child_heights(self):
        if self._has_left_child():
            left_child_height = self.left.height
        else:
            left_child_height = -1
        if self._has_right_child():
            right_child_height = self.right.height
        else:
            right_child_height = -1

        return max(left_child_height, right_child_height)


    # Return balance factor of self 
    def _rebalance(self):
        if self._has_left_child():
            left_child_height = self.left.height
        else:
            left_child_height = -1
        if self._has_right_child():
            right_child_height = self.right.height
        else:
            right_child_height = -1
        return left_child_height - right_child_height

   
    def search(self, key_to_find):
        if key_to_find == self.key:
            return self
        elif self._has_left_child() and key_to_find<=self.key:
            return self.left.search(key_to_find)
        elif self._has_right_child() and key_to_find>self.key:
           return self.right.search(key_to_find)
        else:
            return None
  
    def delete(self, key_to_delete):
        if key_to_delete < self.key:
            if self._has_left_child():
                self.left = self.left.delete(key_to_delete)       
        elif key_to_delete > self.key:
            if self._has_right_child():
                self.right = self.right.delete(key_to_delete)
        elif key_to_delete == self.key:
            if self._is_leaf():
                return None
            elif self._has_left_child() and not self._has_right_child():
                return self.left
            elif self._has_right_child() and not self.has_left_child():
                return self.right
            else:
                new_root = self.right.minimum()
                new_root.right = self.right.delete(new_root.key_to_delete)
                new_root.left = self.left
                return new_root
        return self
              

    def minimum(self):
        if self._has_left_child():
            return self.left.minimum()
        else:
            return self
    
    def _is_leaf(self):
        return not (self._has_left_child() or self._has_right_child())

    def _has_left_child(self):
        return not self.left is None

    def _has_right_child(self):
        return not self.right is None

    
           
