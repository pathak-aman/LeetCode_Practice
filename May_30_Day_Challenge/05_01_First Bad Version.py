# The isBadVersion API is already defined for you.
@param version, an integer
@return a bool
def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start,end = 1,n
        bad_version = None
        while start<=end:
            mid = (start+end)//2
            if isBadVersion(mid):
                bad_version = mid
                end = mid -1
            else:
                start = mid+1
        print(start,bad_version)
        return bad_version



