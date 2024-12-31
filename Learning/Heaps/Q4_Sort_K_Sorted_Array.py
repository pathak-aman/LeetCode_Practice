import heapq

class Solution:
    def sort_k(self, arr, k):
        min_heap = []
        pos = 0
        for i in arr:
            heapq.heappush(min_heap, i)
            if len(min_heap) > k:
                arr[pos] = heapq.heappop(min_heap)
                pos += 1

        while len(min_heap) > 0:
            arr[pos] = heapq.heappop(min_heap)
            pos += 1

        return arr
    
print(Solution().sort_k([6, 5, 3, 2, 8, 10, 9], k = 3))