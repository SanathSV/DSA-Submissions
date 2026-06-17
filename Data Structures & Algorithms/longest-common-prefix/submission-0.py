class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for x in strs[1:]:
            temp =""
            for a,b in zip(x,ref):
                if a==b:
                    temp+=a
                else:
                    break
            ref =temp
        return ref
