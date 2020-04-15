# Done!
class Solution:
    def stringShift2(self, s, shift):
        left = 0
        right = 0
        size = len(s)
        for i in shift:
            if not i[0]:
                left += i[1]
            else:
                right += i[1]
        left %=size
        right%=size
        left = left-right
        # if left > 0:
        #     s = s[left:] + s[0:left]
        # else:
        #     s = s[left:] + s[0:left]
        s = s[left:] + s[0:left]
        return s

    # def fun(self,s,shift):
    #     for i in shift:
    #         if not i[0]:
    #             s = s[i[1]:] + s[0:i[1]]
    #         else:
    #             s = s[-i[1]:] + s[0:-i[1]]
    #     return s

a =  [[1,4],[1,5],[1,4],[1,7],[0,4],[0,7],[1,9]]
obj1 = Solution()
print(obj1.stringShift2('abcdefghijk',a))
# print(obj1.fun('abcdefghijk',a))