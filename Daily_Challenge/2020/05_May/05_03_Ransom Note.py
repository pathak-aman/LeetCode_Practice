class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dict_note = {}
        # for i in ransomNote:
        #     if dict_note.get(i):
        #         dict_note[i]+=1
        #     else:
        #         dict_note[i] =1
        #
        # dict_magazine = {}
        # for i in magazine:
        #     if dict_magazine.get(i):
        #         dict_magazine[i] += 1
        #     else:
        #         dict_magazine[i] = 1
        # for i in dict_note:
        #     if not dict_note.get(i) <= dict_magazine.get(i,0):
        #         return False
        # return True
        #




        for i in set(ransomNote):
            if not ransomNote.count(i) <= magazine.count(i):
                return False
            magazine = magazine.replace(i, "")
        return True




obj1 = Solution()
print(obj1.canConstruct('aaab3a','bbaaatyryhba'))
