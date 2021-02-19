class FirstUnique:

    def __init__(self, nums):
        self.unique_dict = dict()
        for i in nums:
            if i in self.unique_dict:
                self.unique_dict[i] +=1
            else:
                self.unique_dict[i] = 1
        for i in list(self.unique_dict):
            if self.unique_dict[i] > 1:
                self.unique_dict.pop(i)

    def showFirstUnique(self) -> int:
        try:
            return next(iter(self.unique_dict))
        except:
            return -1

    def add(self, value: int) -> None:
        if value in self.unique_dict:
            self.unique_dict.pop(value)
        else:
            self.unique_dict[value] = 1

# Your FirstUnique object will be instantiated and called as such:
nums = [9,9,10,10,10,10,12,17,17,17,12]
obj = FirstUnique(nums)
print(obj.showFirstUnique())
obj.add(7)
obj.add(7)
print(obj.showFirstUnique())
obj.add(9)
print(obj.showFirstUnique())
obj.add(11)
obj.add(9)
obj.add(17)
print(obj.showFirstUnique())

