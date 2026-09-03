class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        word = s.lower()

        while left <= right:
            if not word[left].isalnum():
                left += 1
                continue
            if not word[right].isalnum():
                right -=1 
                continue
            
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        
        return True
