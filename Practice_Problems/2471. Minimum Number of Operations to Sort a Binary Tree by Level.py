from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def num_swap(self, level):
        swaps = 0
        sorted_level = sorted(level)
        visited_array = [0 for i in range(len(level))]
        nums_dict = {sorted_level[i]: i for i in range(len(level))}

        for i in range(len(visited_array)):
            if not level[i] == sorted_level[i] and not visited_array[i]:
                visited_array[i] = 1
                cycle_length = 1
                next = nums_dict[level[i]]
                # next = sorted_level.index(level[i])
                while not level[next] == level[i]:
                    visited_array[next] = 1
                    cycle_length +=1
                    # next = sorted_level.index(level[next])
                    next = nums_dict[level[next]]
                
                swaps += cycle_length - 1
        return swaps


    def minimumOperations(self, root) -> int:
        if not root:
            return 0
        total_swaps = 0
        q = deque()
        q.append(root)

        while len(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total_swaps += self.num_swap(level)    
        return total_swaps

nums = [23,28,20,12,2,6,8,9,10]
print(Solution().num_swap(level=nums))