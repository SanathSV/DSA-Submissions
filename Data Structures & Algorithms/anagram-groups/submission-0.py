class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        large = defaultdict(list)
        for x in strs:
                temp = ''.join(sorted(x))
                large[temp].append(x)
            
        
        res = list()
        for x in large:
            res.append(large[x])
        return res