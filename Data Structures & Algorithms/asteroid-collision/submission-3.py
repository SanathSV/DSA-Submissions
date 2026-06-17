class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = []

        for x in asteroids:
            
            while(a and a[-1] > 0 and x <0):
                if abs(x) == a[-1]:
                    a.pop()
                    break
                elif abs(x) > a[-1]:
                    a.pop()
                    continue
                elif abs(x) < a[-1]:
                    break
            else:
                a.append(x)
        
        return a