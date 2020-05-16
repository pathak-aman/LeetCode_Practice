class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        numbersDeleted = 0
        while numbersDeleted < k:
            if not num:
                return '0'
            elif num[0] == '0':
                num = num[1:]
                continue
            else:
                numberDeletedInThisIteration = False
                posDigit = 0
                while posDigit < len(num)-1:
                    if not num[posDigit+1] > num[posDigit]:
                        num = num[:posDigit]+num[posDigit+1:]
                        print(num)
                        numbersDeleted +=1
                        numberDeletedInThisIteration = True
                        break
                    posDigit+=1

                if not numberDeletedInThisIteration:
                    num = num[1:]
                    numbersDeleted += 1

        if not num:
            return '0'
        elif num[0] == '0':
            num = str(int(num))
            return num
        else:
            return num

obj1 = Solution()
# print(obj1.removeKdigits("34000000000000000000002503245874687567456212378000282365452720487465252173840927251099999999999979037893789678768756564535434565467789908089098097898567456345232341243543564768970980980867564543245123567457457568300000025032456745745756832503245674574575683508768768768730007",27))
print(obj1.removeKdigits('112',1))