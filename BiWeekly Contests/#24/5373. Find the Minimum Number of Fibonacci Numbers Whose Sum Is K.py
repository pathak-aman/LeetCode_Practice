class Solution:
    def findMinFibonacciNumbers1(self, k: int) -> int:
        fibs = [1, 1]
        d = 0
        while d < k:
            d = fibs[-1] + fibs[-2]
            fibs.append(d)
        # print(fibs)
        d = 1
        if k == fibs[-1]:
            return 1
        k-=fibs[-2]
        while k>0:
            for i in range(len(fibs)):
                if fibs[i] == k:
                    # print(fibs[i])
                    d+=1
                    return d
                elif fibs[i] > k:
                    k -= fibs[i-1]
                    # print(fibs[i-1])
                    d+=1
                    break
        return d

    def findMinFibonacciNumbers(self, k: int):
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
        d = 0
        while k>0:
            for i in range(len(fibs)):
                if fibs[i] == k:
                    return d+1
                elif fibs[i] > k:
                    k %= fibs[i-1]
                    d+=1
                    break
        return d




obj1 = Solution()
num = 100000342
print(obj1.findMinFibonacciNumbers1(num))
print(obj1.findMinFibonacciNumbers(num))