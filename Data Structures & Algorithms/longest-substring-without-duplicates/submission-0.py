class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 0

        left = 0
        right = 0
        curr = set()

        while right < len(s):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            
            curr.add(s[right])
            right += 1

            max_len = max(max_len, right - left)
    
        return max_len




        