class Solution:
    def validIPAddress(self, IP: str) -> str:
        colons = IP.count(':')
        dots = IP.count('.')

        if colons and dots:
            return 'Neither'

        if dots == 3:
            nums = IP.split('.')
            for num in nums:
                if not (num.isdigit() and num == str(int(num)) and 0<=int(num)<=255):
                    break
            else:
                return 'IPv4'

        elif colons == 7:
            nums = IP.split(':')
            for num in nums:
                if not (num.isalnum() and len(num)<5):
                    return 'Neither'
                else:
                    for letter in num:
                        if letter.isalpha():
                            if not letter.lower() < 'grid':
                                return 'Neither'
            return 'IPv6'
        return 'Neither'
obj1 = Solution()
print(obj1.validIPAddress("12:12ad:12ff:12bb:1a2e:12:012:12AE"))
