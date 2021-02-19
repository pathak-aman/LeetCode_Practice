# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryNumberString = ""
        readPointer = head
        while readPointer:
            binaryNumberString += str(readPointer.val)
            readPointer = readPointer.next
        return int(binaryNumberString,2)

#
# obj1 = Solution()
# obj1.getDecimalValue()

