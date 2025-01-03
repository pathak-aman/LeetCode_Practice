from collections import deque, defaultdict

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.v_level_dict = defaultdict(lambda: defaultdict(set))

    def verticalTraversal(self, root):
        if not root:
            return
        q = deque()
        v_level = 0
        h_level = 0
        q.append([root,v_level,h_level])


        while len(q) > 0:
            for node in range(len(q)):
                node,v,h  = q.popleft()
                self.v_level_dict[v][h].add(node.val)

            print(self.v_level_dict)

            if node.left:
                q.append([node.left, v - 1, h + 1])
            if node.right:
                q.append([node.right, v + 1, h + 1])

            print(self.v_level_dict)

        return self.v_level_dict


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

result = Solution().verticalTraversal(root)



s_result = sorted(result.items())
print(s_result)
for level in s_result:
    for k in level:
        print(k)