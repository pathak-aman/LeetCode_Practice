# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def search(self,root,val):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.search(root.left,val)
        else:
            return self.search(root.right,val)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)


# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print(Solution().searchBST(root,5).val)
print(Solution().searchBST(root,8).val)
print(Solution().searchBST(root,11))