import numpy as np


class Solution:
    def rotate1(self, matrix) -> None:
        matrix = np.transpose(matrix)
        matrix.tolist()
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                end_column = len(matrix) - 1 - column
                if column <= end_column:
                    matrix[row][column], matrix[row][end_column] = matrix[row][end_column], matrix[row][column]
                else:
                    break

    def rotate(self,matrix):
        skipColumn = 0
        n = len(matrix)
        for iteration in range(n//2):
            start = iteration
            end = n - iteration - 1
            for element in range(skipColumn, n - skipColumn - 1):
                temp = matrix[start][element]
                matrix[start][element] = matrix[end-element +skipColumn][start]
                matrix[end - element +skipColumn][start] = matrix[end][end-element+skipColumn]
                matrix[end][end-element+skipColumn] = matrix[element][end]
                matrix[element][end] = temp
            skipColumn+=1
        print(matrix)
obj1 = Solution()
obj1.rotate([[6,7],[8,9]])
# obj1.rotate(matrix =
# [
#   [ 5, 1, 9,11,17,19],
#   [ 2, 4, 8,10,18,22],
#   [13, 3, 6, 7,36,34],
#   [15,14,12,16,20,21],
#   [32,24,26,29,30,31],
#   [25,23,27,28,33,35],
# ],)

 # obj1.rotate(matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])