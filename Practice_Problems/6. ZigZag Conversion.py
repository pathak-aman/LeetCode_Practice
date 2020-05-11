class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        pos = 0
        output =[""]*numRows
        plus = True

        for letter in s:
            output[pos] = output[pos]+letter

            if pos == numRows-1:
                plus = False
            elif pos == 0:
                plus = True
            if plus:
                pos+=1
            else:
                pos-=1
        outputStr = "".join(output)
        return outputStr

obj1 = Solution()
print(obj1.convert(s = "PAYPALISHIRING", numRows = 1))
