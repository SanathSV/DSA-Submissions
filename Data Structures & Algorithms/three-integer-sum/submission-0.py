class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = 0 
        res = []
        while(l < len(nums)):
            r = l+1
            a = set()
            while(r < len(nums)):
                if -(nums[l] + nums[r]) in a:
                    if sorted([nums[l], nums[r],-(nums[l] + nums[r]) ]) not in res:
                        res.append(sorted([nums[l], nums[r],-(nums[l] + nums[r]) ]))
                else:
                    a.add(nums[r])
                r+=1
            l += 1
        return res