class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for x in strs:
            res += str(len(x))+"#"+x
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        res = []
        n = len(s)

        while(i<n):
            j = i
            while(s[j]!='#'):
                j+=1

            #the length
            length = int(s[i:j])

            # scanning for the word
            # j is at the delimitter #
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end


            
        return res




