class Solution:
    def reformat(self, s: str) -> str:
        count = []
        digits = []
        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                count.append(i)
                
        if abs(len(count)-len(digits)) == 1 or abs(len(count)-len(digits)) == 0:
            output = ''
            if len(count)>len(digits):
                output = count.pop(0)
                first = digits
                second = count

            elif len(count)<len(digits):
                output = digits.pop(0)
                first = count
                second = digits

            else:
                first = count
                second = digits
            print(first,second)
            for i,j in zip(first,second):
                output = output +i+j
            return output
        else:
            return ''

obj1 = Solution()
s = 'ab123'
print(obj1.reformat(s))