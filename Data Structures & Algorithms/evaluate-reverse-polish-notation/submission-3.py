class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = list()
        for x in tokens:
            try:
                nums = int(x)
                a.append(nums)
            except:
                x1 = a.pop()
                x2 = a.pop()
                if x =='+':
                    a.append(x1+x2)
                elif x =='-':
                    a.append(x2-x1)
                elif x =='*':
                    a.append(x2*x1)
                elif x =='/':
                    a.append(int(x2/x1))

                

        return a[0]
                