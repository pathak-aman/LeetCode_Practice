from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_width = 0

    def widthOfBinaryTree(self, root) -> int:
        if not root:
            return True
        level = 1
        q = deque()
        q.append(root)

        while len(q) > 0:
            level_arr = []
            first_non_null = False
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
                    
                    if not first_non_null:
                        # stores start position
                        first_non_null = True
                        start_pos = len(level_arr) - 1
                    else:
                        self.max_width = max(self.max_width, len(level_arr) - 1 - start_pos + 1)




            print(level, level_arr)            
            # if level > 1 and level_arr[:len(level_arr)//2] != level_arr[len(level_arr)//2:][::-1]:
            #     return False
            level += 1
        return self.max_width



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.right.left.right = TreeNode(12)

print(Solution().widthOfBinaryTree(root))