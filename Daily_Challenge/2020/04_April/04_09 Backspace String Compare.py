# # class Solution:
# #     def backspaceCompare(self, S: str, T: str) -> bool:
# #         S = S.replace('#','\b')
# #         T = T.replace('#','\b')
# #         S.encode()
# #
# #         print(T)
# #         return False
# #
# # obj1 = Solution()
# # S = 'ab#c'
# # T = 'ad#c'
# # obj1.backspaceCompare(S,T)
# #
# #
#
# # def s (text):
# #     for i in text:
# #         if i == '#':
# #             print(end='\b')
# #         else:
# #             print(i,end='')
# # S = 'ab#gkjl###c'
# # s(S)
#
#
# from io import StringIO
# import sys
#
# old_stdout = sys.stdout
# sys.stdout = mystdout = StringIO().read('adf\b')# blah blah lots of code ...
#
# sys.stdout = old_stdout
#
# mystdout.getvalue()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Done
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def convert(text):
            answer = []
            for i in text:
                if i != '#':
                    answer.append(i)
                else:
                    if len(answer):
                        answer.pop(len(answer)-1)
            text = "".join(answer)
            return text
        print(convert((S)))
        if convert(S) == convert(T):
            print(convert((S)))
            return True
        else:
            return False
obj1 = Solution()
S = 'ab#d#ckj##l##'
T = 'b#spo'
print(obj1.backspaceCompare(S,T))