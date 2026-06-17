class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_left = []
        array_right = []
        nums_l= [1]+nums
        ar_rev=nums[::-1]

        temp = 1
        for ind , x in enumerate(nums[:]):
            array_left.append(nums_l[ind]*temp)
            temp = array_left[ind]
        
        ar_rev = [1]+ar_rev
        temp = 1
        for ind , x in enumerate(nums[::-1]):
            temp = ar_rev[ind]*temp
            array_left[len(array_left) - ind-1] *= temp 
        
        
        return array_left