class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        rows = row1
        while rows <=row2:
            columns = col1
            while columns <=col2:
                self.rectangle[rows][columns] = newValue
                columns+=1
            rows+=1

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(obj.rectangle)
obj.updateSubrectangle(0,0,3,2,5)
print(obj.rectangle)
print(obj.getValue(0,2))
obj.updateSubrectangle(3,0,3,2,10)
print(obj.rectangle)