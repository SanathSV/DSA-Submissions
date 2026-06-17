class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = []

        arr = list(zip(position,speed))
        arr= sorted(arr, key=lambda x: x[0])
        for x in arr:
            time = (target-x[0])/x[1]

            while(a and time >= a[-1]):
                a.pop()

            a.append(time)

        return len(a)