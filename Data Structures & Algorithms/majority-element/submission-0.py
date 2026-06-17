class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        constraint = len(nums)//2
        a = defaultdict(int)
        for x in nums:
            a[x] +=1
            if a[x] > constraint:
                return x
        