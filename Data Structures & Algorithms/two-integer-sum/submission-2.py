class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for ind,x in enumerate(nums):
            if (target-x) in a:
                return [a[(target-x)],ind]
            a[x]=ind

        return []