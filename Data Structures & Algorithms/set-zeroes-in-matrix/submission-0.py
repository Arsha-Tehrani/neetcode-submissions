class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    right = j + 1
                    left = j - 1
                    up = i - 1
                    down = i + 1
                    #right
                    while right < len(matrix[0]):
                        if matrix[i][right] == 0:
                            right += 1
                            continue
                        matrix[i][right] = "x"
                        right += 1
                    
                    #left
                    while left >= 0:
                        if matrix[i][left] == 0:
                            left -= 1
                            continue
                        matrix[i][left] = "x"
                        left -= 1

                    #Down
                    while down < len(matrix):
                        if matrix[down][j] == 0:
                            down += 1
                            continue
                        matrix[down][j] = "x"
                        down += 1

                    #Up
                    while up >= 0:
                        if matrix[up][j] == 0:
                            up -= 1
                            continue
                        matrix[up][j] = "x"
                        up -= 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0

        return None



        