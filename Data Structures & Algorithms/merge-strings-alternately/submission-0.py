class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        length = 0
        if len(word1)>len(word2):
            temp = word1
            length = len(word2)
        else:
            temp = word2
            length = len(word1)

        for x,y in zip(word1,word2):
            res += f"{x}{y}"

        return res+temp[length:]