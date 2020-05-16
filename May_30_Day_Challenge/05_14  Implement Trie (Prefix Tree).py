class Trie:

    def __init__(self):
        self.dictwords = dict()

    def insert(self, word: str) -> None:
        if self.dictwords.get(word):
            self.dictwords[word] +=1
        else:
            self.dictwords[word] = 1

    def search(self, word: str) -> bool:
        if word in self.dictwords.keys():
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.dictwords.keys():
            if key.startswith(prefix):
                return True
            else:
                return False
