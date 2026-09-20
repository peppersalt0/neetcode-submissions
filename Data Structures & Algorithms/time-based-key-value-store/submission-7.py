from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hsh = defaultdict(list)
    # timestamp, value
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hsh[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hsh[key]
        if not arr:
            return ""
        lo = 0
        hi = len(arr) - 1

        while lo < hi:
            mid = -(-(lo + hi) // 2)
            if arr[mid][0] <= timestamp:
                lo = mid
            else:
                hi = mid - 1
        
        return arr[lo][1] if arr[lo][0] <= timestamp else ""
