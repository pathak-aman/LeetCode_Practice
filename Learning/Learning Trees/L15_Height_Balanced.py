# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def find_depth(root):
            if not root:
                return 0
            left_height = find_depth(root.left)
            right_height = find_depth(root.right)

            if left_height == -1:
                return -1
            if right_height == -1:
                return -1

            if abs(left_height-right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
            
        return find_depth(root) != -1
        




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
print(Solution().isBalanced(root))