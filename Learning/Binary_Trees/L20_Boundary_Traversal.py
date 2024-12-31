class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.result = []


    def isLeaf(self, node):
        return not node.left and not node.right

    def left_boundary(self, root):
        curr = root
        while curr:
            if not self.isLeaf(curr):
                self.result.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def right_boundary(self, root):
        curr = root
        right_order = []
        while curr:
            if not self.isLeaf(curr):
                right_order.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        self.result.extend(right_order[::-1])

    def leaf_boundary(self, root):
        if not root:
            return
        if self.isLeaf(root):
            self.result.append(root.val)
            
        self.leaf_boundary(root.left)
        self.leaf_boundary(root.right)


    def boundary_traversal(self, root):
        self.left_boundary(root)
        print(self.result)
        self.leaf_boundary(root)
        print(self.result)
        self.right_boundary(root)
        return self.result[:-1:]


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)



root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.right = Node(4)
root.left.left.right.left = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.left.left = Node(10)
root.right.right.left.right = Node(11)



print(Solution().boundary_traversal(root))