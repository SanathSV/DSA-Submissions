class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        r = 0 
        f = 0 
        max_ = 0
        while(r < len(s)):
            while(s[r] in a):
                
                a.remove(s[f])
                f += 1
            a.add(s[r])
            max_ = max(max_ , len(a))
            r+=1
        return max_

