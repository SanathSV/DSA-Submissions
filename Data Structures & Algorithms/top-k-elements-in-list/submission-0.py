class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = defaultdict(int)

        for x in nums:
            A[x] += 1

        Z = sorted(A.items(),key= lambda item: item[1], reverse =True)
        Z = list(x[0] for x in Z)
        return Z[:k]

        

            