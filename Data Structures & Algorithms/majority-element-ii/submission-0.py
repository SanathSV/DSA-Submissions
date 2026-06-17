class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ref = set(nums)
        a = defaultdict(int)

        for x in nums:
            a[x] +=1
        res = []
        n = len(nums)//3
        for x in ref:
            if a[x] > n:
                res.append(x)

        return res