class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        str_dict = {
            'c':1,
            'r':2,
            'o':3,
            'a':4,
            'k':5
        }
        temp=[]
        for i in croakOfFrogs:
            temp.append(str_dict[i])
        ans = 0
        count = 1
        while temp:
            i = 0
            temp1 = temp.copy()
            while i < len(temp) and temp:
                if temp[i] == count:
                    count+=1
                    if count == 6:
                        ans+=1
                        count=1
                    temp.pop(i)
                else:
                    i+=1
            if temp == temp1:
                return -1
        if count == 1:
            return ans
        else:
            return -1


obj1 = Solution()
croakOfFrogs = "crocraokcrakocrocroakakak"
print(obj1.minNumberOfFrogs(croakOfFrogs))