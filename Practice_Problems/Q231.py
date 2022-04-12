# Power of two


# return n > 0 and (n & n-1 == 0)




class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = abs(n)
        if n < 0:
            return False
        bin_n = bin(n)[2:]
        if '1' in bin_n[1:] or bin_n[0] == '0':
            return False
        else:
            return True
obj = Solution()
r = [2**i for i in range(10)]
r.extend([20,30,41,2,1,7,10])
for f in r:
    print(f, obj.isPowerOfTwo(f))