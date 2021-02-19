class Solution:
    def reformatDate(self, date: str) -> str:
        monthLookUP = {"Jan" : "01", "Feb" :"02", "Mar":"03", "Apr" :"04",
                       "May":"05", "Jun":"06", "Jul":"07", "Aug":"08",
                       "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        splitDate = date.split()
        day = splitDate[0][:-2]
        if len(day) == 1:
            day = "0"+day
        return splitDate[2]+'-'+monthLookUP[splitDate[1]]+'-'+day
obj1 = Solution()
print(obj1.reformatDate(date = "1st May 1960"))



