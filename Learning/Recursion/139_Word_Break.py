from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(index, current_word, wordDict, s):
            if index == len(s):
                if current_word == "":
                    return True
                return False
            current_word += s[index]
            if current_word in wordDict:
            # pick
                if helper(index+1, "", wordDict, s):
                    return True
            # not pick
            if helper(index+1, current_word, wordDict, s):
                return True
            
            return False

        return helper(0,"", wordDict, s)




if __name__ == "__main__":
    # s = "leetcode"
    # wordDict = ["leetc", "co","ode", "de"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(s,wordDict))