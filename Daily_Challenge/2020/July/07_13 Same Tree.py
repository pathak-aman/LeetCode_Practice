# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.array = []

    def traversalPreorder(self, root: TreeNode):
        rootPointer = root
        self.array.append(rootPointer.val)
        if rootPointer.left:
            self.traversalPreorder(rootPointer.left)
        else:
            self.array.append(rootPointer.left)
        if rootPointer.right:
            self.traversalPreorder(rootPointer.right)
        else:
            self.array.append(rootPointer.right)

    def printTree(self, clearAfter=True):
        print(self.array)
        if clearAfter:
            self.array.clear()


class Solution:
    isSame = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.foo(p,q)
        return self.isSame

    def foo(self,p,q):
        if p.val == q.val:
            if p.left and q.left:
                self.foo(p.left, q.left)
            else:
                if not p.left is None and q.left is None:
                    self.isSame =  False

            if p.right and q.right:
                self.foo(p.right, q.right)
            else:
                if not p.right is None and q.right is None:
                    self.isSame = False
        else:
            self.isSame = False


tree = Tree()
tree.root = TreeNode(val=3)
tree.root.left = TreeNode(val=4)
tree.root.left.left = TreeNode(val=1)
tree.root.left.left.left = TreeNode(8)
tree.root.right = TreeNode(val=6)
tree.root.right.right = TreeNode(val=5)
tree.root.right.right.right = TreeNode(val=7)

tree2 = Tree()
tree2.root = TreeNode(val=3)
tree2.root.left = TreeNode(val=4)
tree2.root.left.right = TreeNode(val=1)
tree2.root.left.right.left = TreeNode(8)
tree2.root.right = TreeNode(val=6)
tree2.root.right.right = TreeNode(val=5)
tree2.root.right.right.right = TreeNode(val=7)


obj1 = Solution()
print(obj1.isSameTree(tree.root, tree2.root))
