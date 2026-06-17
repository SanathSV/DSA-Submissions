class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        a = deque()
        for x in operations:
            try:
                num = int(x)
                a.append(num)
            except:
                if x == '+':
                    x1=a[-1]
                    x2=a[-2]
                    a.append(x1+x2)

                elif x == 'C':
                    a.pop()
                elif x == 'D':
                    
                    a.append(a[-1]*2)
            print(a)

        return sum(a)