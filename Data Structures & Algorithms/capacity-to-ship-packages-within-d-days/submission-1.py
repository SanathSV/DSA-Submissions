class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while(l<r):
            mid = (l+r)//2
            days_proj = 0 
            
            count = 0
            for x in weights:
                count+=x
       
                if count > mid:
                    days_proj+=1
                    count = x
            if count:
                days_proj +=1
            
            if days_proj <= days:
                r = mid
            else:
                l = mid+1

        return l