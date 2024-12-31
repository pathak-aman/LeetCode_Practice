# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def maxDepth(self, root:TreeNode) -> int:
        def count_depth(root):
            if not root:
                return 0
            return 1 + max(count_depth(root.left), count_depth(root.right))
        return count_depth(root)
    

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.right.right = TreeNode(78)
root.left.left.left = TreeNode(-2)
root.right.right.left = TreeNode(27)
root.left.left.left.right = TreeNode(89)


print(Solution().maxDepth(root))