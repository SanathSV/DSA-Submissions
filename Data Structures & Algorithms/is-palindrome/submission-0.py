class Solution:
    def isPalindrome(self, s: str) -> bool:
        chrs = ''
        for x in s:
            if x.isalnum():
                chrs +=x.lower()
        print(chrs)
        return chrs == chrs[::-1]