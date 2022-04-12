class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t or s=='':
            return True
        if len(t)<len(s):
            return False

        pos_t,pos_s = 0,0
        while pos_t < len(t):
            if t[pos_t] == s[pos_s]:
                if pos_s == len(s)-1:
                    return True
                else:
                    pos_s+=1
            pos_t+=1
        return False
obj1 = Solution()
print(obj1.isSubsequence('','qrfggtgruhiueetfeewyedwrtrsg'))
