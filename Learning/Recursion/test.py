from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min = float("inf")
        self.previous = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def helper_inorder(root):
            print(root)
            if root is None: 
                return
            print(root.val)
            helper_inorder(root.left)
            if not self.previous is None:
                self.min = int(min(self.min, abs(root.val - self.previous)))
                print(";;;;;;;;", self.min)
            self.previous = root.val
            print("PREEEEEEEEE", self.previous)
            helper_inorder(root.right)
        
            
        helper_inorder(root)
        print(self.min)

        return int (self.min)
    

root = TreeNode()
root.right = TreeNode(val=2)

print(Solution().minDiffInBST(root))