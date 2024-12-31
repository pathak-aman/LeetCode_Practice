# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0
        
    def count_diameter(self, root):
        if not root:
            return 0
        lh = self.count_diameter(root.left)
        rh = self.count_diameter(root.right)

        self.max_diameter = max(self.max_diameter, lh + rh)
        return 1 + max(lh,rh)

    def diameterOfBinaryTree(self, root) -> int:
        self.count_diameter(root)
        return self.max_diameter
    

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.right.right = TreeNode(78)
root.left.left.left = TreeNode(-2)
root.right.right.left = TreeNode(27)
root.left.left.left.right = TreeNode(89)

#               10
#           5           2
#        1                       78
#     -2                    27
#           89
print(Solution().diameterOfBinaryTree(root))