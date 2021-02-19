class Solution:
    def reverseBits(self, n: int) -> int:
        binaryString = bin(n)[2:]
        print(binaryString,len(binaryString))
        binaryString = "0" * (32-len(binaryString)) + binaryString
        print(binaryString,len(binaryString))
        return int(binaryString[::-1],2)
obj1 = Solution()
print(obj1.reverseBits(43261596))
