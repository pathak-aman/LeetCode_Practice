class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        position = 1
        for words in sentence.split():
            if words.startswith(searchWord):
                return position
            position+=1
        return -1
obj1 = Solution()
print(obj1.isPrefixOfWord("hello from the other side", searchWord = "they"))
