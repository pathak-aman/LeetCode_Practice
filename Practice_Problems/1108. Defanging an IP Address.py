class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=address.replace(".","[.]")
        return address
obj1 = Solution()
print(obj1.defangIPaddr("1.1.1.1"))
