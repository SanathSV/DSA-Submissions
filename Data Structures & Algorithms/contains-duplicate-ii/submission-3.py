class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0 
        n = len(nums)
        a = set()
        

        while(r < k):
            if nums[r] in a:
                return True

            a.add(nums[r])
            r += 1

        
        while(r < n):
            if nums[r] in a:
                return True
            a.add(nums[r])
            a.remove(nums[l])
            l+=1
            r+=1

        return False