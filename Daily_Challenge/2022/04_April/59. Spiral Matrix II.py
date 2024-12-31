from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total_cycles = (n + 1) // 2
        result = [[0] * n for i in range(n)]

        number = 1
        for cycle in range(total_cycles):
            # Right-Left
            for i in range(cycle, n - (2 * cycle)):
                result[cycle][i] = number
                number += 1

            for i in range(cycle + 1, n - (2 * cycle)):
                result[i][n - 1 - cycle] = number
                number += 1

            for i in range(n-2-cycle, cycle-1, -1):
                result[n - 1 - cycle][i] = number
                number +=1

            for i in range(n):
                pass



            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))


print(Solution().generateMatrix(n=6))

