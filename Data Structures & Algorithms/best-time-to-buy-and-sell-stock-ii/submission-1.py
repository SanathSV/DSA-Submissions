class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        start = prices[0]
        for x in prices[1:]:
            if start - x < 0 :
                res += (start) - x
            start = x
        
        return abs(res)