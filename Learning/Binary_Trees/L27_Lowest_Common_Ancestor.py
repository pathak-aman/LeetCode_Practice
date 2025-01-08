# We can reuse the previous code and make two path searches from the the root. 2 O(N), O(N)
# Better solution exists with just one traversal and no extra space.
# We will look for both the node values in one shot.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def traverse(self, root, p, q):
        if not root:
            return False
        if root.val == p or root.val == q:
            return root.val
        
        # left traverse
        l = self.traverse(root.left, p, q)

        # right traverse
        r = self.traverse(root.right, p,q)

        # Both False
        if not l and not r:
            return l

        # Both True: Ancestor found! return its value
        if l and r:
            return root.val
        
        # left not null, right null
        if l and not r:
            return l

        # right not null, left null
        if r and not l:
            return r 
        
    def lowestCommonAncestor(self, root, p, q):
        return self.traverse(root,p,q)
    

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


print(Solution().lowestCommonAncestor(root, 5,1))




    
        