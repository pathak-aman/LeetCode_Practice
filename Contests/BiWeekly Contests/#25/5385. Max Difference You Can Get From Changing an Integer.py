# class Solution {
#  public int getMaxNum(int n) {
#        String sN = ""+n;
#        int minNum = 11;
#        for(int i=0;i<sN.length();i++) {
#           if(sN.charAt(i) != '9') {
#               minNum = Integer.parseInt("" + sN.charAt(i));
#               break;
#           }
#        }
#        if(minNum != -1)
#            return Integer.parseInt(sN.replaceAll(""+minNum,"9"));
#        else
#            return  n;
#    }
#    public int getMinNum(int n) {
#        String sN = ""+n;
#        if(sN.charAt(0) == '1') {
#            int i;
#            for(i=0;i<sN.length();i++)
#                if(sN.charAt(i)!='1' && sN.charAt(i)!='0')
#                    break;
#            if(i > sN.length() - 1 ) return n;
#            return Integer.parseInt(sN.replaceAll("" + sN.charAt(i), "0"));
#        }
#        else {
#           return Integer.parseInt(sN.replaceAll(""+sN.charAt(0),"1"));
#        }
#    }
#    public int maxDiff(int num) {
#
#        return getMaxNum(num)-getMinNum(num);
#    }
# }


class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        first_non_ = '9'
        for i in str_num:
            if i!='9':
                first_non_ = i
                break
        a = str_num.replace(first_non_,'9')

        if str_num[0]!='1':
            b = str_num.replace(str_num[0],'1')
        else:
            first_non_ = '0'
            for i in str_num:
                if i > '1':
                    first_non_ = i
                    break
            b = str_num.replace(first_non_,'0')
        # print(a,b)
        return int(a)-int(b)

obj1 = Solution()
print(obj1.maxDiff(num = 60062329))


