# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def f(self, p, i):
        print(p,i)
        root_node = p[0]
        inorder_root_index = i.index(root_node)

        left_i = i[:inorder_root_index]
        right_i = i[inorder_root_index+1:]

        left_p = p[1:inorder_root_index+1]
        right_p = p[inorder_root_index+1:]

        if len(left_i) and len(left_p):
            left_node = self.f(left_p, left_i)
        else:
            left_node = None
        if len(right_i) and len(right_p):
            right_node = self.f(right_p, right_i)
        else:
            right_node = None

        return TreeNode(root_node, left_node, right_node)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        return self.f(preorder, inorder)

    def traversal(self, root: Optional[TreeNode]) -> Optional[List[int]]:
        if not root:
            return None
        self.traversal(root.left)
        print(root.val)
        self.traversal(root.right)




if __name__ == '__main__':
    p = [10,20,40,50,30,60]
    i = [40,20,50,10,60,30]

    tree = Solution().buildTree(p,i)
    Solution().traversal(tree)
