class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sumM = [[0] * (C+1) for _ in range(R+1)]

        for r in range(R):
            pre = 0
            for c in range(C):
                pre += matrix[r][c]
                above = self.sumM[r-1][c]
                self.sumM[r][c] = pre + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        buttom = self.sumM[row2][col2]
        above = self.sumM[row1 - 1][col2]
        left = self.sumM[row2][col1-1]
        upper_l = self.sumM[row1-1][col1-1] 
        return buttom-above-left+upper_l

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)