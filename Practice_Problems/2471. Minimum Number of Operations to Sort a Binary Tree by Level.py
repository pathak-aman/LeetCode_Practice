

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

        for i in range(len(visited_array)):
            if level[i] != sorted_level[i] and not visited_array[i]:
                visited_array[i] = 1
                cycle_length = 1
                cycle_index = sorted_level.index(level[i])
                while level[cycle_index] != level[i]:
                    visited_array[cycle_index] = 1
                    cycle_length +=1
                    cycle_index = sorted_level.index(level[cycle_index])
                    swaps += cycle_length - 1
                return swaps


    def minimumOperations(self) -> int:
        self.swaps = 0

nums = [68020, 77092, 24805, 46436, 18824, 54086, 31847, 1214, 23978, 12234, 38254, 22523, 68727]
print(Solution().num_swap(level=nums))