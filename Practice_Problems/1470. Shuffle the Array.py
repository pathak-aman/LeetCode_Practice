class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        output = [0]*2*n
        i,j,k = 0,n,0
        while k < 2*n:
            output[k] = nums[i]
            k+=1
            i+=1
            output[k] = nums [j]
            j+=1
            k+=1
        return output
obj1 = Solution()
print(obj1.shuffle([1,2,3,4,5,6,8,9],4))
