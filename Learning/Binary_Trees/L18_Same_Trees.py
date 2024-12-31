# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(p,q):
            if (not p and q) or (not q and p):
                return False
            elif not p and not q:
                return True
            else:
                if p.val == q.val:
                    return preorder(p.left, q.left) and preorder(p.right, q.right)
                else:
                    return False
        return preorder(p,q)