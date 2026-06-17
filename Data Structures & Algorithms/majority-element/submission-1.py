class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        constraint = len(nums)//2
        nums.sort()
        return nums[constraint]
        