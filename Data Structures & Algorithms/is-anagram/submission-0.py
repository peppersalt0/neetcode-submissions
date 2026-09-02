class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shsh = {}
        thsh = {}

        for c in s:
            shsh[c] = shsh.get(c, 0) + 1
        
        for c in t:
            thsh[c] = thsh.get(c, 0) + 1

        return shsh == thsh