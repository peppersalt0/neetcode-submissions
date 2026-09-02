class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hsh:
                hsh[sorted_word] = []
            hsh[sorted_word].append(word)
        
        return list(hsh.values())



        