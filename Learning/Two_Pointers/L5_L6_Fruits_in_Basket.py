# Longest subarray with atmost k types of elements.
class Solution:
    def fruits_in_basket(self, arr, k):
        l,r = 0,0
        max_length = 0
        fruit_freq = {}

        while r < len(arr):
            # Add
            fruit_freq[arr[r]] = fruit_freq.get(arr[r],0) + 1

            # Invalidity
            
            if len(fruit_freq) > k:
                while len(fruit_freq) > k:
                    fruit_freq[arr[l]] -= 1
                    if fruit_freq[arr[l]] == 0:
                        fruit_freq.pop(arr[l])
                    l += 1

            # Validity + Max_len
            if len(fruit_freq) <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
    

class Solution_2:
    def fruits_in_basket(self, arr, k):
        l,r = 0,0
        max_length = 0
        fruit_freq = {}

        while r < len(arr):
            # Add
            fruit_freq[arr[r]] = fruit_freq.get(arr[r],0) + 1

            # Invalidity
            if len(fruit_freq) > k:
                fruit_freq[arr[l]] -= 1
                if fruit_freq[arr[l]] == 0:
                    fruit_freq.pop(arr[l])
                l += 1

            # Validity + Max_len
            if len(fruit_freq) <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
    

arr = [1,3,1,2,2,2,1,1,3,1,3,3,2,2,3,3,1]
k = 2
print(Solution().fruits_in_basket(arr,k))
print(Solution_2().fruits_in_basket(arr,k))