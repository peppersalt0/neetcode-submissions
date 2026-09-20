class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        

        def inSH(mid, hi):
            if nums[mid] <= nums[hi]:
                return True
            else:
                return False


        while lo < hi:
            mid = (lo + hi) // 2
            if inSH(mid, hi):
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo]