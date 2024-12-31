from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helperfunc(node, sequence_list):
            if node:
                if node.left is None and node.right is None:
                    sequence_list.append(node.val)
            else:
                return 

            helperfunc(node.left, sequence_list)
            helperfunc(node.right, sequence_list)


        
        sequence_1 = []
        sequence_2 = []
        print(helperfunc(root1, sequence_1))
        helperfunc(root2, sequence_2)
        print(sequence_1, sequence_2)
        return sequence_1 == sequence_2

# [3,5,1,6,2,9,8,null,null,7,4]
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right  = TreeNode(8)
root1.left.right.left  = TreeNode(7)
root1.left.right.right = TreeNode(4)


root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(7)
root1.right.left = TreeNode(4)
root1.right.right  = TreeNode(2)
root1.right.right.left  = TreeNode(9)
root1.right.right.right = TreeNode(8)

print(Solution().leafSimilar(root1, root1))