class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = 0

        a = []
        res = [0]*len(temperatures)
        for ind,x in enumerate(temperatures):
            element = [x,ind]
            while(a and a[-1][0] < x):
                y = a.pop()
                res[y[1]] = abs(y[1] - ind)

            else:
                a.append(element)

        return res