class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in hsh:
                hsh[key] = []
            hsh[key].append(word)
        
        return list(hsh.values())



        