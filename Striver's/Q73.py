# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            print(matrix[i])

        row_zero_pos = set()
        col_zero_pos = set()

        # O(n^2)
        for row, array in enumerate(matrix):
            for col, element in enumerate(array):
                if not element:
                    row_zero_pos.add(row)
                    col_zero_pos.add(col)

        print(row_zero_pos)
        print(col_zero_pos)

        for row in row_zero_pos:
            matrix[row] = [0] * m

        for row in range(n):
            for col in col_zero_pos:
                matrix[row][col] = 0

        for i in range(n):
            print(matrix[i])


obj = Solution()
obj.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])