class Solution:
    def isValid(self, s: str) -> bool:
        hsh = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []

        for c in s:
            if c in hsh:
                if not stack or hsh[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return not stack
