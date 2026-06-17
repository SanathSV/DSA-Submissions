class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fwd = 0 
        last = len(nums) - 1

        for ind in range(len(nums)):
            
            if nums[ind] == 2 :
                while(last > 0 and nums[last]==2):
                    last-=1
                if ind>last:
                    break
                print("2_",ind,last)
                nums[last],nums[ind]=nums[ind],nums[last]
                last -=1
            if nums[ind] == 0:
                print("1_",ind,fwd)
                nums[fwd],nums[ind]=nums[ind],nums[fwd]
                fwd +=1
            
            