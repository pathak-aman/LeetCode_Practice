from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.parent_pointer = dict()


    def get_Parent_Pointer(self, root):
        if not root:
            return 
        
        q = deque()
        q.append(root)

        while len(q) > 0:
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    self.parent_pointer[node.left.val] = node
                if node.right:
                    q.append(node.right)
                    self.parent_pointer[node.right.val] = node
        return self.parent_pointer
    
    def minimum_time_to_burn(self, root, target):
        parent_pointer = self.get_Parent_Pointer(root)
        time = 0
        q = deque()
        q.append(target)

        visited = set()

        while len(q) > 0:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                
                if node.left:
                    if not node.left.val in visited:
                        q.append(node.left)
                if node.right:
                    if not node.right.val in visited:
                        q.append(node.right)
                if node.val in parent_pointer:
                    if not parent_pointer[node.val].val in visited:
                        q.append(parent_pointer[node.val])
            if len(q) > 0:
                time += 1
        return time

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


print(Solution().minimum_time_to_burn(root, root.left))