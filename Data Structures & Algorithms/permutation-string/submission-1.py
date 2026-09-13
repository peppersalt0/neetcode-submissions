class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        string1 = [0] * 26
        string2 = [0] * 26

        for c in s1:
            string1[ord(c) - 97] += 1
        
        for i in range(len(s1) - 1):
            string2[ord(s2[i]) - 97] += 1
                
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            string2[ord(s2[right]) - 97] += 1
            right += 1
            
            if string1 == string2:
                return True

            string2[ord(s2[left]) - 97] -= 1
            left += 1

        
        return False
         