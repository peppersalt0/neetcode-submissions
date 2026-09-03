class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        pre = 0
        for i in range(len(height)):
            pre = max(pre, height[i])
            prefix[i] = pre
        
        suf = 0
        for i in range(len(height) - 1, -1, -1):
            suf = max(suf, height[i])
            suffix[i] = suf

        res = [0] * len(height)

        for i in range(len(height)):
            res[i] = min(prefix[i], suffix[i]) - height[i]
        
        return sum(res)

        # pre 
        # 0, 2, 2, 3, 3, 3, 3, 3, 3, 3

        # suf
        # 3, 3, 3, 3, 3, 3, 3, 3, 2, 1

        # res
        # 0, 0, 2, 0, 2, 3, 2, 0, 0, 0