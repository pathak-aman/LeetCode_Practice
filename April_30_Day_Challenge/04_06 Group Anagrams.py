# Done!
class Solution:
    def groupAnagrams(self, strs):
        ana_dict = dict()
        for i in strs:
            temp = tuple(sorted(i))
            if temp in ana_dict.keys():
                ana_dict[temp].append(i)
            else:
                ana_dict[temp] = [i]
        return list(ana_dict.values())

obj1=Solution()
d = obj1.groupAnagrams(strs= ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"])
print(d)