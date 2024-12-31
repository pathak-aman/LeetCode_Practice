# Definition for a binary tree node.
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    
    # root, left, right
    def preorder(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    # root, left, right
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    # root, left, right
    def postorder(self, root, arr):
        if not root:
            return
        self.postorder(root.left, arr)
        self.postorder(root.right, arr)
        arr.append(root.val)

    def levelorder(self, root, level, q):
        if not root:
            return
        q.append(root)

        while len(q) > 0:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level.append(current_level)


    def traversal_helper(self, root):
        pre = []
        ino = []
        post = []
        level = []
        q = deque()
        self.preorder(root, pre)
        self.inorder(root,ino)
        self.postorder(root, post)
        self.levelorder(root, level,q)

        return f'Preorder: {pre}\nInorder: {ino}\nPostorder: {post}\n Level: {level}'

root = Node(10)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(1)
root.right.right = Node(78)

print(Solution().traversal_helper(root))