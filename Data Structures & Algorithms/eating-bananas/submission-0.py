class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def canEat(rate):
            hours = 0
            for pile in piles:
                if rate >= pile:
                    hours += 1
                else:
                    hours += -(-pile // rate)
            return hours <= h


        while lo < hi:
            mid = (lo + hi) // 2
            if canEat(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo