# Numbers at most N given digit set

from math import comb

class Solution:
    def binary_search(self, array, item):
        start, end = 0, len(array)
        while start < end:
            mid = (start + end)//2
            if array[mid] == item:
                return mid
            elif array[mid] > item:
                end = mid-1
            else:
                start = mid+1
        return -1

    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        digits_in_N = len(str(n))
        numbers = len(digits)
        sum = [(comb(numbers, 1)) ** i for i in range(1, digits_in_N - 1)]


        for place,num in enumerate(str(n)):
            pos = self.binary_search(digits, num)
            if pos == -1:



obj = Solution()
item = obj.binary_search([1,2,4,6,8,9], 5)
print(item)