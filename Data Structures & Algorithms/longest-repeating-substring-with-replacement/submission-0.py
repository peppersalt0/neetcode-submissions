class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hsh = {}

        left = 0
        longest = 0
        max_count = 0

        for right in range(len(s)):
            hsh[s[right]] = hsh.get(s[right], 0) + 1
            max_count = max(max_count, hsh[s[right]])
            while max_count <= right - left - k:
                hsh[s[left]] = hsh.get(s[left], 0) - 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest
