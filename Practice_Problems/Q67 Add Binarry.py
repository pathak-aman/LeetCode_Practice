class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # answer = ""
        # carry = 0
        # if len(a) > len(b):
        #     big_string = a
        #     longest_string = len(a)
        # else:
        #     big_string = b
        #     longest_string = len(b)
        #
        # for i, j in zip(reversed(a), reversed(b)):
        #     sum = carry + int(i) + int(j)
        #     if sum >= 2:
        #         carry = 1
        #     if sum % 2 == 0:
        #         answer += "0"
        #     else:
        #         answer += "1"
        #     longest_string -= 1
        # print(longest_string)
        # while carry != 0 and longest_string > 0:
        #     sum = carry + int(big_string[len(big_string) - 1 - longest_string])
        #     if sum >= 2:
        #         carry = 1
        #     if sum % 2 == 0:
        #         answer += "0"
        #     else:
        #         answer += "1"
        #     longest_string -= 1

        # if carry == 1:
        #     answer += "1"
        #
        # if longest_string > 0:
        #     print(big_string[-longest_string::-1])
        #     answer += big_string[-longest_string::-1]
        # return answer[::-1]

        answer = ""
        carry = 0
        len_diff = abs(len(a)-len(b))
        if len(a) >= len(b):
            b = "0" * len_diff + b
        else:
            a = "0" * len_diff + a

        for i,j in zip(reversed(a), reversed(b)):
            summation = int(i) + int(j) + carry
            if summation >= 2:
                carry = 1
            else:
                carry = 0

            if summation % 2 == 0:
                answer += "0"
            else:
                answer += "1"
        if carry == 1:
            answer += "1"
        return answer[::-1]


obj = Solution()
# print(obj.addBinary("1100","1110"))
print(obj.addBinary("1010", "1011"))
