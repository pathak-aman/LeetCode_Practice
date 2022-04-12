# Q118. Pascal's Triangle
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        output = [[1],[1,1]]
        for n in range(2, numRows):
            temp_output = [1]
            sum = [output[n-1][i] + output[n-1][i-1] for i in range(1, len(output[n-1]))]
            temp_output.extend(sum+[1])
            output.append(temp_output)
        return output

obj = Solution()
print(obj.generate(10))