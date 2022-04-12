class Solution:
    def canJump(self, nums) -> bool:
        is_zero = False
        zero_count = 0
        print(nums)
        print(nums[len(nums)-2::-1])
        for i in nums[len(nums)-2::-1]:
            if i == 0:
                is_zero = True
                zero_count +=1
            elif is_zero:
                if i > zero_count+1:
                    is_zero = False
                    zero_count = 0
                else:
                    zero_count+=1
        if is_zero:
            if i == len(nums)-1:
                return True
            return False
        return True

obj1 = Solution()
array = [4,4,0,0,2,0,3,0,2,0,1]
print(obj1.canJump(array))
