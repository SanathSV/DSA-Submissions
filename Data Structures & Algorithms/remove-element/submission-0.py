class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fwd = 0
        for ind,x in enumerate(nums):
            if x!=val:
                nums[fwd] = x
                fwd +=1
        return fwd