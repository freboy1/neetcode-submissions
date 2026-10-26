class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])
        low, high = 0, (n*m) - 1

        while low <= high:
            
            mid = (low + high) // 2

            n_r = mid // m
            n_c = mid % m

            if matrix[n_r][n_c] == target:
                return True
            elif matrix[n_r][n_c] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False