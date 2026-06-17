class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        a = defaultdict(int)
        b = defaultdict(int)
        if len(s1) > len(s2):
            return False
        l,r=0,0
        for x in s1:
            a[x] +=1

        while(r < k):
            b[s2[r]] +=1
            r+=1

        if a==b:
            return True
        

        while(r < len(s2)):
            b[s2[l]] -=1
            l +=1
            b[s2[r]] +=1
            r+=1
            e = 0
            for x in a:
                if a[x] != b[x]:
                    e = 1
            if e == 0 :
                return True
        

        return False

