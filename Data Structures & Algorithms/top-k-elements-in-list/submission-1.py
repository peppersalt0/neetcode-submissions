import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}

        for num in nums:
            hsh[num] = hsh.get(num, 0) - 1
        
        heap = []

        for key, val in hsh.items():
            heapq.heappush(heap, (val, key))
        
        res = []

        for i in range(k):
            res.append(heap[0][1])
            heapq.heappop(heap)

        return res
        
