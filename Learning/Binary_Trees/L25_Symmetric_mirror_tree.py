from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        level = 1
        q = deque()
        q.append(root)

        while len(q) > 0:
            level_arr = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    level_arr.append("NULL")
                else:
                    if node.left: 
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
                    
                    level_arr.append(node.val)

            # print(level, level_arr)            
            if level > 1 and level_arr[:len(level_arr)//2] != level_arr[len(level_arr)//2:][::-1]:
                return False
            level += 1
        return True