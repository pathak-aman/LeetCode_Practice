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

    def findnode(self, root, value):
        if not root:
            return
        if root.val == value:
            return root
        
        lh = self.findnode(root.left, value)
        rh = self.findnode(root.right, value)

        return lh or rh
    
    def get_Parent_Pointer(self, root):
        if not root:
            return 
        
        q = deque()
        q.append(root)
        bfs = []

        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    self.parent_pointer[node.left.val] = node
                if node.right:
                    q.append(node.right)
                    self.parent_pointer[node.right.val] = node
                level.append(node.val)
            bfs.append(level)
        return self.parent_pointer
    

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

result_dict = Solution().get_Parent_Pointer(root)
for k,v in result_dict.items():
    print(k, v.val)

print(Solution().findnode(root, 4).val)