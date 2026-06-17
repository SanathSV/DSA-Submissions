class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        sum_ = 0

        while(r < len(prices)):
            sum_ = max(prices[r] - prices[l],sum_)
            if prices[r] < prices[l]:
                l = r
            r+=1
            

        return sum_


        
            
            