# Problem Statement: Given a Binary Tree and a reference to a root belonging to it. Return the path from the root node to the given node.
# No two nodes in the tree have the same data value.
# It is assured that the given node is present and a path always exists.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = []

    def traverse(self, root, node):
        if not root:
            return False
        self.path.append(root.val)
        if root.val == node:
            return True
        
        found_left = self.traverse(root.left, node)
        if found_left:
            return True
               
        found_right = self.traverse(root.right, node)
        if found_right:
            return True
        
        # if not found_left and not found_right:
        #     self.path.pop()
        self.path.pop()


    





root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
print(Solution().getPath(root, 5))
print(Solution().getPath(root, 1))
print(Solution().getPath(root, 8))
print(Solution().getPath(root, 6))
print(Solution().getPath(root, 7))