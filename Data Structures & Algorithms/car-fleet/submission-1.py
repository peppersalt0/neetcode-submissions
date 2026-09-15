class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for i in range(len(position)):
            times.append((position[i], (target - position[i]) / speed[i]))
        
        times.sort()

        # times will be sorted by position first desc the time it takes
        # stack, while we find a speed that is equal or smaller then we can pop 
        # return the size of the array after everything has been popped

        res = []

        for car in times:
            while res and car[1] >= res[-1][1]:
                res.pop()
            res.append(car)
        
        return len(res)

