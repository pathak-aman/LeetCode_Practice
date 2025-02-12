from collections import defaultdict
import heapq
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        digit_sum_dict = defaultdict(list)

        for num in nums:
            elem = num
            digit_sum = 0
            while num:
                num, digit = divmod(num, 10)
                digit_sum += digit

            heapq.heappush(digit_sum_dict[digit_sum], elem)
            if len(digit_sum_dict[digit_sum]) > 2:
                heapq.heappop(digit_sum_dict[digit_sum])

        for heap in digit_sum_dict.values():
            if len(heap) == 2:
                ans = max(ans, heap[0] + heap[1])
        return ans