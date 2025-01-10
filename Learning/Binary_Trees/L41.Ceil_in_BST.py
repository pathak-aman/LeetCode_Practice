# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.ceil = -1
    def search_ceil(self,root,val):
        if not root:
            return None
        if root.val == val:
            self.ceil = root.val
            return root
        elif root.val > val:
            self.ceil = root.val
            return self.search_ceil(root.left,val)
        else:
            return self.search_ceil(root.right,val)
    def searchBST(self, root: Optional[TreeNode], val: int):
        self.search_ceil(root,val)
        return self.ceil


# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print(Solution().searchBST(root,6))
print(Solution().searchBST(root,8))
print(Solution().searchBST(root,0))
print(Solution().searchBST(root,1))
print(Solution().searchBST(root,9))
print(Solution().searchBST(root,11))