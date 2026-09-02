class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq = [[] for _ in range(max(counts.values()) + 1)]

        for key, val in counts.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)

        return res