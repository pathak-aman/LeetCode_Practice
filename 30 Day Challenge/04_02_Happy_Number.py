
"""Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

# Done!


# class Solution:
#     def isHappy(self, n):
#         str_n = str(n)
#         sq = {'0': 0,
#               '1': 1,
#               '2': 4,
#               '3': 9,
#               '4': 16,
#               '5': 25,
#               '6': 36,
#               '7': 49,
#               '8': 64,
#               '9': 81
#               }
#         add = 0
#         end = {'4','29','25','16','37','58','89','145','42','20'}
#         for i in str_n:
#             add += sq[i]
#         add = str(add)
#         print(str_n, add)
#         if add[0] == '1' and add[1:].count('0') == len(add) - 1:
#             return True
#         elif add in end:
#             return False
#         else:
#             return self.isHappy(int(add))
#
#
# obj1 = Solution()
# print(obj1.isHappy(25))

class Solution:
    def isHappy(self, n):
        while n >= 10:
            add = 0
            for i in str(n):
                add += int(i)**2
            n = add
        # print(n)
        if n == 1 or n==7:
            return True
        else:
            return False
obj1 = Solution()
print(obj1.isHappy(89))

