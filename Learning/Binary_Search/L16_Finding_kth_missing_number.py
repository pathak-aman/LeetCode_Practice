# Brute O(N)
def brute(nums, k):
    for i in nums:
        if i <= k:
            k += 1
        else:
            return k

# BS - O(logN)
def BS(nums, k):
    missing_nums = []
    for i in range(len(nums)):
        missing_nums.append(nums[i] - (i+1))

    l,r = 0, len(missing_nums)
    # while l <= r:
    #     mid = (l+r)//2
    #     if missing_nums[mid] == k: # Don't do this, won;t be able to find the correct mid, as there might be duplicates.
    #         break
    #     elif missing_nums[mid] < k:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # if l > r:
    #     return nums[r] + (k - r)
    # else:
    #     return nums[mid] - 1



def BS_striver(nums, k):
    l, r = 0, len(nums)
    while l <= r:
        mid = (l+r)//2
        missing_value_before_mid = nums[mid] - (mid + 1)
        if missing_value_before_mid < k:
            l = mid + 1
        else:
            r = mid - 1
    # As the while loop ends, l and r while cross each other such that l = r + 1

    
    # nums[r] + more
    # nums[r] + k - missing_value_before_r
    # nums[r] + k - (nums[r] - (r + 1))
    # r + 1 + k
    # Since l = r + 1, therefore we can also return l + k

    return r + 1 + k
    

nums = [2,3,4,7,11]
k = 6

# nums = [4,7,9]
# k = 3
print(BS_striver(nums, k))