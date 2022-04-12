from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        self.n = len(self.nums)

    def find_pos(self, val: int) -> int:
        low, high = 0, self.n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.nums[mid] == val:
                return mid
            elif self.nums[mid] > val:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def add(self, val: int) -> int:
        self.nums.insert(self.find_pos(val), val)
        self.n += 1
        return self.nums[-self.k]


nums = [1, 2, 3, 4, 5, 10, 12, 13]
k = 3

sol = KthLargest(k, nums)
query = [3, 6, 19, 21, 17,15,24, -1, 5, 39, 55]
for i in query:
    print("Pos for ", i, "is :", sol.find_pos(i))
    print("largest", sol.add(i))
    print(sol.nums)
