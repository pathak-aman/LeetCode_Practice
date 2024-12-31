class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurence(arr,target):
            l = 0
            r = len(arr)-1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] < target:
                    l = mid+1
                    ans = mid
                else:
                    r = mid-1
            # print(l,r,ans)
            if l == len(arr) or arr[l] != target:
                return -1
            return l
            # if ans >= len(arr) -1:
            #     return -1
            # elif arr[ans+1] != target:
            #     return -1
            # return ans + 1

        # Last occurrence: Largest index with element equal to target
        def lastOccurence(arr,target):
            l = 0
            r = len(arr)-1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] > target:
                    r = mid-1
                    ans = mid
                else:
                    l = mid+1
            # print(l,r,ans)
            if r == len(arr) or arr[r] != target:
                return -1
            return r


        if nums == []:
            return  [-1,-1]
        return [firstOccurence(nums, target), lastOccurence(nums, target)]

if __name__ == '__main__':
    arr = [5,5,5,5,7,7,7,7, 8, 8, 8,8,8,8,9,9,9,9,9,10,12,12,14,15,16, 16,16,20]
    target = 90

    # target = 6
    print(firstOccurence(arr,target))
    print(lastOccurence(arr,target))