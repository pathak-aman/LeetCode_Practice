class Solution:
    def pancakeSort(self, A: list) -> list:
        output = []
        toBePlacedElement = len(A)
        while toBePlacedElement:
            currentPosition = A.index(toBePlacedElement)
            if currentPosition == toBePlacedElement-1:
                pass
            elif currentPosition == 0:
                A[:toBePlacedElement] = reversed(A[:toBePlacedElement])
                output.append(toBePlacedElement)
            else:
                A[:currentPosition+1] = reversed(A[:currentPosition+1])
                A[:toBePlacedElement] = reversed(A[:toBePlacedElement])
                output.extend([currentPosition+1,toBePlacedElement])
            toBePlacedElement -=1
        return output

obj1  = Solution()
print(obj1.pancakeSort(A = [5,3,2,8,9,10,7,4,1,6]))
