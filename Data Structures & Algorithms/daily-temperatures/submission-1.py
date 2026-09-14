class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [temperature, index]
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return res

        # stack = [(47, 5)(76, 7)(100, 8)]
        # res = [2, 1, 1, 0, 0]