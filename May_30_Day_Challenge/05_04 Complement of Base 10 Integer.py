class Solution:
    def findComplement(self, num: int) -> int:
        # num = bin(num).replace('0b','')
        # i = 0
        # answer = ''
        # while i <len(num):
        #     if num[i] == '0':
        #         answer += '1'
        #     else:
        #         answer += '0'
        #     i+=1
        # return int(b,2)


        #
        # b = bin(num)[2:]
        # b = b.replace('0', '2')
        # b = b.replace('1', '0')
        # b = b.replace('2', '1')
        # return int(b, 2)
        #

        # num = bin(num)[2:]
        # return int(num.translate(num.maketrans('01','10')),2)

        b_str = bin(num).replace('0b', '')
        mask_str = ''.join(['1'] * len(b_str))
        d = num ^ int(mask_str, 2)
        return d
obj1 = Solution()
print(obj1.findComplement(5))

