class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        start = prices[0]
        for x in prices[1:]:
            if start - x < 0 :
                res +=  x-(start)
            start = x
        
        return res