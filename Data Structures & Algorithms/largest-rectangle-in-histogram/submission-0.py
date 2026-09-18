class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # (index, height)
        res = 0

        for i in range(len(heights)):
            replaced = -1
            while stack and heights[i] < stack[-1][1]:
                res = max(res, (i - stack[-1][0]) * stack[-1][1])
                replaced = stack[-1][0]
                stack.pop()
            
            stack.append((replaced if replaced != -1 else i, heights[i]))
        

        while stack:
            res = max(res, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()
        
        return res