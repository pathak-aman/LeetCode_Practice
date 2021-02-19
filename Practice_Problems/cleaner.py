# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # A function to implement recursion that validates a node in BST

        def checkValidNode(node, low=-math.inf, high=math.inf):
            # Happy flow
            if not node:
                return True
            # Invalid node
            if node.val <= low or node.val >= high:
                return False
            # Validate left and right nodes
            return (checkValidNode(node.left, low, node.val) and
                    checkValidNode(node.right, node.val, high))

        return checkValidNode(root)
