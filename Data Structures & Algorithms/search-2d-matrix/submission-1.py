class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        row = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] == target:
                row = mid
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        row = hi
        lo = 0
        hi = len(matrix[row]) - 1

        if row != -1:
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        return False

        


