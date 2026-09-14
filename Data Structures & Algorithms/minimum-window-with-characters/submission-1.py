class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shsh = {}
        thsh = {}

        for c in t:
            thsh[c] = thsh.get(c, 0) + 1

        have = 0
        need = len(thsh)
        shortest = float('infinity')
        res = []

        l = 0
        for r in range(len(s)):
            if s[r] in thsh:
                shsh[s[r]] = shsh.get(s[r], 0) + 1
                if shsh.get(s[r], 0) == thsh.get(s[r], 0):
                    have += 1
            while have == need:
                length = r - l + 1

                if length < shortest:
                    shortest = length
                    res = [l, r]
                if s[l] in thsh:
                    shsh[s[l]] = shsh.get(s[l], 0) - 1
                    if shsh.get(s[l], 0) < thsh.get(s[l], 0):
                        have -= 1
                l += 1
        
        if not res:
            return ""
        else:
            return s[res[0]:res[1] + 1]
                


