class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = set()
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                starts.add(num)
        
        for start in starts:
            curr = start
            curr_len = 0
            while curr in num_set:
                curr_len += 1
                curr += 1
            longest = max(curr_len, longest)
        
        return longest