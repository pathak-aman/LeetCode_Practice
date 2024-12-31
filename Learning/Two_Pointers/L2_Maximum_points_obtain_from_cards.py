class Solution():
    def max_points(self, arr, k):
        # Initialzing the max_sum to be the sum of first k elements
        l_sum = sum(arr[:k])
        print(l_sum)
        r_sum = 0
        max_sum = l_sum

        r = len(arr) - 1
        for l in range(k-1, -1, -1):
            l_sum -= arr[l]
            r_sum += arr[r]
            print(l,l_sum)
            print(r,r_sum)

            max_sum = max(max_sum, l_sum + r_sum)
            print(max_sum)
            r -= 1
    
        return max_sum



arr = [2,3,4,6,7,1,2,9,3,6,7]
k = 4
print(Solution().max_points(arr, k))