class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        low, high = 0, len(matrix) - 1
        n_r = -1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                n_r = mid
                break
        
        if n_r == -1:
            return False

        low, high = 0, len(matrix[mid])

        while low <= high:

            mid = (low + high) // 2

            if matrix[n_r][mid] == target:
                return True
            elif matrix[n_r][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False