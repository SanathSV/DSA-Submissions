class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)
        if len(s)!=len(t):
            return False
        for x,y in zip(s,t):
            a[x]+=1
            b[y]+=1
        return a==b