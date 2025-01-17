# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def search_insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.search_insert(root.right, val)
        else:
            root.left = self.search_insert(root.left, val)
        return root
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search_insert(root, val)


# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print(Solution().insertIntoBST(root,9))
print(Solution().insertIntoBST(root,100))
print(Solution().insertIntoBST(root,20))
print(Solution().insertIntoBST(root,11))
print(Solution().insertIntoBST(root,9))
print(Solution().insertIntoBST(root,1))