class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # if x==y:
        #     return 0
        # elif x > y:
        #     y = bin(y)[2:]
        #     x = bin(x)[2:]
        #     y = '0'*(len(x)-len(y))+ y
        #
        # else:
        #     y = bin(y)[2:]
        #     x = bin(x)[2:]
        #     x = '0' * (len(y) - len(x)) + x
        # print(x,y)
        # output = 0
        # for xi,yi in zip(x,y):
        #     if int(xi)^int(yi):
        #         output+=1
        # return output

        x = x^y
        return bin(x)[2:].count('1')
obj1 = Solution()
print(obj1.hammingDistance(23,70))
