class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0 ,0
        sum_ = 0
        len_= float('inf')

        while(r < len(nums)):
            sum_ += nums[r]
            while(sum_ >= target):
                len_ = min(len_,(r-l+1))
                sum_ -= nums[l]
                l+=1
                print(len_,r)
            r+=1

        if len_ == float('inf'):
            len_ = 0
        return len_