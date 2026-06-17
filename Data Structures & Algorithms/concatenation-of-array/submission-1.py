class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = len(nums)
        for x in range(len(nums)):
            nums.append(nums[x])
        return nums