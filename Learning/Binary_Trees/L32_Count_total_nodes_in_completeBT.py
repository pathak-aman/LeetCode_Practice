# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root):
        # No nodes when null
        if not root:
            return 0

        lh = self.find_left_height(root.left)
        rh = self.find_right_height(root.right)

        if lh == rh:
            return 1 << lh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def find_left_height(self, root):
        height = 0
        curr = root
        while curr:
            height += 1
            curr = curr.left
        return height

    def find_right_height(self, root):
        height = 0
        curr = root
        while curr:
            height += 1
            curr = curr.right
        return height
