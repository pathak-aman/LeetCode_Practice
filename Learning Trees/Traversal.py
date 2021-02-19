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

    def traversalPreorder(self,root:TreeNode):
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

    def traversalInorder(self,root:TreeNode):
        rootPointer = root
        if rootPointer.left:
            self.traversalInorder(rootPointer.left)
        else:
            self.array.append(rootPointer.left)
        self.array.append(rootPointer.val)
        if rootPointer.right:
            self.traversalInorder(rootPointer.right)
        else:
            self.array.append(rootPointer.right)

    def traversalPostorder(self,root:TreeNode):
        rootPointer = root
        if rootPointer.left:
            self.traversalPostorder(rootPointer.left)
        else:
            self.array.append(rootPointer.left)
        if rootPointer.right:
            self.traversalPostorder(rootPointer.right)
        else:
            self.array.append(rootPointer.right)
        self.array.append(rootPointer.val)

    def printTree(self, clearAfter = True):
        print(self.array)
        if clearAfter:
            self.array.clear()


tree = Tree()
tree.root = TreeNode(val = 3)
tree.root.left = TreeNode(val = 4)
tree.root.left.left = TreeNode(val = 6)
tree.root.right = TreeNode(val = 5)
tree.root.right.left = TreeNode(val = 8)
tree.root.right.right = TreeNode(val = 7)

tree.traversalPreorder(tree.root)
print('Preorder traversal : ')
tree.printTree()
tree.traversalInorder(tree.root)
print('Inorder traversal : ')
tree.printTree()
tree.traversalPostorder(tree.root)
print('Postorder traversal : ')
tree.printTree()
# print(tree.array)
# # class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: