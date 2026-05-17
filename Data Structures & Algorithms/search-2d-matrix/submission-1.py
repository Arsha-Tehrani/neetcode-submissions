class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            middle = l + int((r-l)/2)
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                l_row = 0
                r_row = len(matrix[middle])-1
                while l_row <= r_row:
                    m = l_row + int((r_row-l_row)/2)
                    if matrix[middle][m] > target:
                        r_row = m - 1
                    elif matrix[middle][m] < target:
                        l_row = m + 1
                    else:
                        return True
                return False

            elif target > matrix[middle][-1]:
                l = middle + 1

            elif target < matrix[middle][0]:
                r = middle - 1

        return False
            