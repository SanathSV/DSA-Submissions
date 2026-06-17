class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        # here the thing is that we move to the right , and if the total duplicate count is k then peace
        a = defaultdict(int)
        len_ = 0 
        while(r < len(s)):
            temp = 0 
            a[s[r]] += 1
            for x in a: #find the max string kaa length
                temp = max(temp , a[x])

            while((r-l+1)-temp > k):
                a[s[l]] -= 1
                l+=1

            
            len_ = max(len_ , r-l+1)
            r+=1
        return len_