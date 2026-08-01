class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        go = True
        j = 0
        i = -1
        total = len(matrix) * len(matrix[0])
        count = 0
        while go:
            #Right
            i += 1
            while i < len(matrix[0]):
                #print(j, i)
                if matrix[j][i] == "x":
                    break
                res.append(matrix[j][i])
                count += 1
                matrix[j][i] = "x"
                i += 1
            i -= 1
            
            
            j += 1
            #Down
            while j < len(matrix):
                #print(j, i)
                if matrix[j][i] == "x":
                    break
                res.append(matrix[j][i])
                count += 1
                matrix[j][i] = "x"
                j += 1
            j -= 1

            #Left
            i -= 1
            while i >= 0:
                #print(j, i)
                if matrix[j][i] == "x":
                    break
                res.append(matrix[j][i])
                count += 1
                matrix[j][i] = "x"
                i -= 1

            i += 1

            #Up
            j -= 1
            while j >= 0:
                #print(j, i)
                if matrix[j][i] == "x":
                    break
                res.append(matrix[j][i])
                count += 1
                matrix[j][i] = "x"
                j -= 1
            j += 1

            if count == total:
                go = False

        return res
