class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_left(root)
    
    def push_left(self, root):
        curr = root
        while curr:
           self.stack.append(curr)
           curr = curr.left
    
    def next(self):
        node = self.stack.pop()
        if node.right:
            self.push_left(node.right)
        return node.val

    def has_next(self):
        if self.stack:
            return True
        else:
            return False


# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)


iter = BSTIterator(root)
print(iter.has_next())
print("next()", iter.next())
print(iter.has_next())
print("next()", iter.next())
print(iter.has_next())
print("next()", iter.next())
print(iter.has_next())
print("next()", iter.next())
print(iter.has_next())
print("next()", iter.next())
print(iter.has_next())
print("next()", iter.next())

