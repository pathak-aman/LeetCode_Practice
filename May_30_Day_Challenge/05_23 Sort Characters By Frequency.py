class Solution:
    def frequencySort(self, s: str) -> str:
        lettersInString = set(list(s))
        occurrenceLettersDict = dict()
        for letter in lettersInString:
            count = s.count(letter)
            if occurrenceLettersDict.get(count):
                occurrenceLettersDict[count].append(letter)
            else:
                occurrenceLettersDict[count] = [letter]
        outputString = ''
        for key in sorted(occurrenceLettersDict.keys(),reverse=True):
            for lettersInKeys in occurrenceLettersDict[key]:
                outputString+=lettersInKeys*key
        return outputString


obj1 = Solution()
print(obj1.frequencySort('Aaaabbsllddeirooskijhdksassaass'))

