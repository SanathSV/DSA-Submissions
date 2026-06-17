class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0 ,len(people) - 1
        res = 0 
        people.sort()
        while(l <= r):
            diff = limit - people[r]
            print(diff, r,people[r])
            r -= 1
            res += 1
            if l <= r and diff >= people[l]: #hence these two can make up a pair and go on
                l+=1

        return res
            

