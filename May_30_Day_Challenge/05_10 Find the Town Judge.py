class Solution:
    def findJudge(self, N: int, trust) -> int:
        leftTracker = [0]*N
        rightTracker = [0]*N
        for singleTrust in trust:
            leftTracker[singleTrust[0]-1] +=1
            rightTracker[singleTrust[1] - 1] += 1
        try:
            f = rightTracker.index(N-1)
            if leftTracker[f] == 0:
                return f+1
        except:
            return -1
        return -1

    def findJudge1(self, N: int, trust) -> int:
        if len(trust) and N ==1:
            return 1
        leftTracker = dict()
        rightTracker = dict()

        for singleTrust in trust:
            if not leftTracker.get(singleTrust[0]):
                leftTracker[singleTrust[0]] = 1
            if rightTracker.get(singleTrust[1]):
                rightTracker[singleTrust[1]] +=1
            else:
                rightTracker[singleTrust[1]] = 1
        for key,value in rightTracker.items():
            if value == N-1:
                if not leftTracker.get(key):
                    return key
                break
        return -1


obj1 = Solution()
print(obj1.findJudge( N = 1, trust = []))
print(obj1.findJudge1( N = 1, trust = []))