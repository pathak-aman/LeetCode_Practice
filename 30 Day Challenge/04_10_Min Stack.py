# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.top_ptr = -1
#
#     def print_status(self):
#         print('Stack : ',self.stack)
#         print('Top at :',self.top_ptr)
#
#     def push(self, x: int) -> None:
#         self.top_ptr +=1
#         self.stack.append(x)
#         self.print_status()
#
#     def pop(self) -> None:
#         if self.top_ptr >= 0:
#             self.stack.pop(self.top_ptr)
#             self.top_ptr-=1
#         self.print_status()
#
#     def top(self) -> int:
#         if self.top_ptr >= 0:
#             return self.stack[self.top_ptr]
#         else:
#             return 'Underflow'
#
#     def getMin(self) -> int:
#         if self.top_ptr>=0:
#             return min(self.stack)


# obj.push(4)
# print('Min Element : ',obj.getMin())
# print('Top elemnet : ',obj.top())
# obj.pop()
# print('Top elemnet : ',obj.top())
# obj.push(5)
# print('Top elemnet : ',obj.top())
# obj.push(14)
# print('Min Element : ',obj.getMin())
# obj.pop()
# print('Top elemnet : ',obj.top())
# obj.push(43)
# obj.pop()
# obj.pop()
# print('Top elemnet : ',obj.top())
# obj.push(42)
# obj.push(46)
# # param_3 = obj.top()
# print(obj.getMin())
'''Version 2'''
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.top_ptr = -1
#
#     def push(self, x: int) -> None:
#         self.top_ptr +=1
#         self.stack.append(x)
#
#     def pop(self) -> None:
#         if self.top_ptr >= 0:
#             # self.stack.pop(self.top_ptr)
#             self.top_ptr-=1
#
#     def top(self) -> int:
#         if self.top_ptr >= 0:
#             return self.stack[self.top_ptr]
#
#
#     def getMin(self) -> int:
#         if self.top_ptr>=0:
#             return min(self.stack[0:self.top_ptr+1])

# Your MinStack object will be instantiated and called as such:

'''Version 3'''
from math import inf


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.top_ptr = -1
        self.min = inf

    def push(self, x: int) -> None:
        if x < self.min:
            self.min = x
        self.top_ptr += 1
        self.stack.extend([x])

    def pop(self) -> None:
        if self.top_ptr >= 0:
            f = self.stack.pop(self.top_ptr)
            self.top_ptr -= 1
            if f == self.min:
                self.min = inf
                for i in self.stack:
                    if i < self.min:
                        self.min = i
                # print("Previous min : ",f,"Now :",self.min)

    def top(self) -> int:
        if self.top_ptr >= 0:
            return self.stack[self.top_ptr]

    def getMin(self) -> int:
        if self.top_ptr >= 0:
            return self.min

minStack = MinStack()
minStack.push(5)
minStack.pop()
minStack.push(0)
minStack.push(-8)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
minStack.push(-4)
minStack.push(-8)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
