# class Solution {
#    public int longestSubarray(int[] nums, int limit) {
#        if(nums.length == 0) return 0;
#        int maxCount = 1;
#        int cMin,cMax;
#        for(int i=0;i<nums.length;i++) {
#            int count = 0;
#            cMin = nums[i];
#            cMax = nums[i];
#            Boolean cont = true;
#            int j;
#            for(j=i;j<nums.length && cont;j++) {
#                if(cMin > nums[j]) cMin = nums[j];
#                if(cMax < nums[j]) cMax = nums[j];
#                if(Math.abs(cMin-cMax)>limit) cont = false;
#                else count++;
#            }
#            if(maxCount < count)
#                maxCount = count;
#            if(i+maxCount >= nums.length) return  maxCount;
#        }
#        return maxCount;
#    }
# }