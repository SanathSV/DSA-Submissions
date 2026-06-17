class Solution:
    def isValid(self, s: str) -> bool:
        a = {
            '}' :'{',
            ']':'[',
            ')':'('
            }
        stack = list()

        for x in s:
            
            if x in a and (not stack or stack[-1] != a[x]):
                return False
            elif x in a and stack[-1] == a[x]:
                stack.pop()
            else:
                stack.append(x)
            
        return len(stack)==0