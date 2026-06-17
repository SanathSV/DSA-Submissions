class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fwd = 0 
        rec = 0
        while(rec < len(nums)):
            nums[fwd] = nums[rec]

            while(rec < len(nums) and nums[rec] == nums[fwd]):
                rec +=1
            fwd +=1
            

        return fwd