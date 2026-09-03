class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        res = 0
        while left < right:
            if lmax < rmax:
                res += lmax - height[left]
                left += 1
                lmax = max(lmax, height[left])
            else:
                res += rmax - height[right]
                right -= 1
                rmax = max(rmax, height[right])
        
        return res