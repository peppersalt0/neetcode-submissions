class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for tgt in range(len(nums)):
            if tgt > 0 and nums[tgt] == nums[tgt - 1]:
                continue
            left = tgt + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -nums[tgt]:
                    res.append([nums[left], nums[right], nums[tgt]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[left] + nums[right] < -nums[tgt]:
                    left += 1
                elif nums[left] + nums[right] > -nums[tgt]:
                    right -= 1       
        return res
 
                    