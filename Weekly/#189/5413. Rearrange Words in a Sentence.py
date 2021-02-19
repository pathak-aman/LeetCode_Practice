class Solution:
    def arrangeWords(self, text: str) -> str:
        words_length_dict = {}
        text[0].lower()
        text_split = text.split()
        text_split[0] = text_split[0].lower()
        for word in text_split:
            if words_length_dict.get(len(word)):
                words_length_dict[len(word)] += " " + word
            else:
                words_length_dict[len(word)] = word
        # print(words_length_dict)
        output_text = ""
        for sorted_key in sorted(words_length_dict.keys()):
            output_text += words_length_dict[sorted_key]
            output_text += " "
        return output_text.strip().capitalize()



obj1 = Solution()
print(obj1.arrangeWords('Good bad hello jhefihifhie gy uyg yiu pwodpo vshuqvs kidhow drtderw doiuhoibsiq odwiu1opi'))


