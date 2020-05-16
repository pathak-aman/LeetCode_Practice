class Solution:
    def simplifiedFractions(self, n: int):
        if n == 1:
            return []
        else:
            output = []
            calc = []
            for numerator in range(1,n):
                for denominator in range(numerator+1, n+1):
                    if not numerator/denominator in calc:
                        calc.append(numerator/denominator)
                        output.append("{0}/{1}".format(numerator,denominator))
            return output


obj1 = Solution()
print(obj1.simplifiedFractions(n=12))

