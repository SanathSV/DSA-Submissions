class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a = 0
        for x in piles:
            a = max(a,x)

        # from 1->a is our target
        l = 1 
        r = a
        def check(mid):
            hours = 0 
            for p in piles:
                hours += math.ceil(p / mid)
            return hours

        while(l<r):
            mid = (l+r)//2
            val = check(mid)
            if val <= h:
                r = mid 
            else:
                l = mid + 1

        return l