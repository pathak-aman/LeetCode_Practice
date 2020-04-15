from collections import Counter
class Solution:
    def countElements(self, arr):
        dict_arr = {}
        for i in sorted(arr):
            if i in dict_arr:
                dict_arr[i] +=1
            else:
                dict_arr[i]=1
        print(dict_arr)
        for i in range(len(dict_arr.keys()):
            if dict_arr[i] - dict_arr.keys()[i] == 1 :

arr = [9,34,545,54,6,55,21,-22,-90,1,1,3,3,5,5,7,7]
obj1 = Solution()
obj1.countElements(arr)