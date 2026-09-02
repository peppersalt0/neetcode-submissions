class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}

        for i in range(len(nums)):
            curr = nums[i]
            comp = target - curr

            if comp in hsh:
                return [hsh[comp], i]
            
            else:
                hsh[curr] = i
        
        return []