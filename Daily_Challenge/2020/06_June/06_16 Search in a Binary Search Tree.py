# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    treenodeObject = None

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.foo(root, val)
        return self.treenodeObject

    def foo(self, root, val):
        if root:
            if root.val == val:
                self.treenodeObject = root

            elif root.val > val:
                self.searchBST(root.left, val)

            else:
                self.searchBST(root.right, val)