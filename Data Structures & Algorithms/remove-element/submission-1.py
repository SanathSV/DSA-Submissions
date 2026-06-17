class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fwd = 0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[fwd] = nums[x]
                fwd +=1
        return fwd