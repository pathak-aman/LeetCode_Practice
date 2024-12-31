class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        
        def bouquets_possible(bloomDay, mid, m ,k):
            bouquets, count = 0, 0
            for i in bloomDay:
                if i <= mid:
                    count += 1
                else:
                    bouquets += count // k
                    count = 0
            bouquets += count // k
            return bouquets >= m


        l = 1
        r = max(bloomDay)
        min_day = r
        while l <= r:
            mid = (l + r) // 2
            if bouquets_possible(bloomDay, mid, m, k):
                min_day = min(min_day, mid)
                r = mid - 1
            else:
                l = mid + 1
        return min_day
    

print(Solution().minDays([7,7,7,7,12,11,13,7,7,7], 2,3))