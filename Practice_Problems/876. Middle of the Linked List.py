# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        pointerTwoSteps = head
        pointerOneStep = head

        while pointerTwoSteps or pointerTwoSteps.next:
            pointerTwoSteps = pointerTwoSteps.next
            pointerOneStep = pointerOneStep.next
            print(pointerTwoSteps)
            print(pointerOneStep)
        return pointerOneStep
