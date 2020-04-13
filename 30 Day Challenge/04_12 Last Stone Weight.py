# DONE!
from sortedcontainers import SortedDict
from collections import Counter


class Solution:
    def lastStoneWeight(self, stones):
        stones_sorted_dict = SortedDict(Counter(stones))
        # print(stones_sorted_dict)
        while len(stones_sorted_dict) != 1:
            last = None

            while len(stones_sorted_dict) > 0:
                q = stones_sorted_dict.popitem()
                if q[1] % 2:
                    last = q[0]
                if last:
                    break
            if len(stones_sorted_dict) == 0:
                if last is None:
                    return 0
                else:
                    return last

            second_last = stones_sorted_dict.peekitem()[0]
            stones_sorted_dict[second_last] -= 1

            if stones_sorted_dict[second_last] == 0:
                stones_sorted_dict.popitem()

            q = last - second_last

            if q in stones_sorted_dict:
                stones_sorted_dict[q] += 1

            else:
                stones_sorted_dict[q] = 1

            # print(stones_sorted_dict)

        if len(stones_sorted_dict) == 1:
            if stones_sorted_dict.peekitem()[1] % 2:
                return stones_sorted_dict.peekitem()[0]
            else:
                return 0
obj1 = Solution()
# stones = [4, 4, 4, 5, 6, 4, 5, 2, 5, 7, 4, 67, 3, 65, 3, 3, 45, 54, 76, 42]
stones = [10,100,1000,10000,5,67,977,977]
print(obj1.lastStoneWeight(stones))
