# Inituition: BFS, brute force - check all 26 possibilities at all the positions in the string

from collections import deque

class Solution:

    def bfs(self, beginWord, endWord, set_words):
        q = deque()
        q.append((beginWord,1))
        if beginWord in set_words:
            set_words.remove(beginWord)

        while q:
            for _ in range(len(q)):
                word, step = q.popleft()
                if word  == endWord:
                    return step
                for pos in range(len(word)): #len(beginWords) * 26
                    for i in range(26):
                        new_word = word[:pos] + chr(97 + i) + word[pos+1:]
                        if new_word in set_words:
                            q.append((new_word, step + 1))
                            set_words.remove(new_word)
                # print(q)
        return 0
                 

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_words = set(wordList)
        return self.bfs(beginWord, endWord, set_words)