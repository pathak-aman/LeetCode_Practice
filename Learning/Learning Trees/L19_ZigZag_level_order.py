from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        ans = []
        while len(queue) > 0:
            level_val = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                ans.append((level_val)[::-1])
            else:
                ans.append((level_val))
            level += 1
        return ans``