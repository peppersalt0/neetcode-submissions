class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        shsh, thsh = {}, {}

        for i in range(len(s)):
            shsh[s[i]] = shsh.get(s[i], 0) + 1
            thsh[t[i]] = thsh.get(t[i], 0) + 1

        return shsh == thsh