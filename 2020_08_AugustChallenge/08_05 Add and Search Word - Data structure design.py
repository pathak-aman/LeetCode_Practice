import re
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lenWordsDictionary = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if self.lenWordsDictionary.get(len(word)):
            self.lenWordsDictionary[len(word)].add(word)
        else:
            self.lenWordsDictionary[len(word)] = {word}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if self.lenWordsDictionary.get(len(word)):
            for toBeMatched in self.lenWordsDictionary[len(word)]:
                if re.match(word,toBeMatched):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.search("pad")
obj.search("bad")
obj.search(".ad")
obj.search("")
