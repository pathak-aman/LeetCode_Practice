class Solution:
    def average(self, salary) -> float:
        return (sum(salary) - min(salary) - max(salary))/(len(salary)-2)

obj1 = Solution()
print(obj1.average(salary = [8000,9000,2000,3000,6000,1000]))
