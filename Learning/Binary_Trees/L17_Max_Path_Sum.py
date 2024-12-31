# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = 0

    def DFS_sum(self, root):
        # Leaves have no value
        if not root:
            return 0
        l_sum = self.DFS_sum(root.left)
        r_sum = self.DFS_sum(root.right)
        
        path_sum = l_sum + r_sum + root.val
        # store max value
        self.maxSum = max(self.maxSum, path_sum)

        return path_sum


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.DFS_sum(root)
        return self.maxSum

