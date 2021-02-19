class Solution:
    def toLowerCase(self, str: str) -> str:
        outputString = ''
        # for letter in str:
        #     asciiValue = ord(letter)
        #     if 65 <= asciiValue <= 90:
        #         letter = chr(asciiValue+32)
        #     outputString+=letter
        outputString = ''.join([chr(ord(c)+32) if 65<=ord(c)<=90 else c for c in str])
        return outputString
obj1 = Solution()
print(obj1.toLowerCase('AOVELYZ'))

