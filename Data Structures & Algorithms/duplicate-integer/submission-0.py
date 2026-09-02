class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh = set()

        for num in nums:
            if num in hsh:
                return True
            else:
                hsh.add(num)
        
        return False