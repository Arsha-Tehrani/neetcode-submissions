class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        temp = set()
        visited.add((0,0))
        n = len(grid)-1
        res = grid[0][0]
        sys.setrecursionlimit(10000)

        def add(i, j, water_lvl):
                    if i < 0 or i > n or j < 0 or j > n or water_lvl < grid[i][j] or (i, j) in visited or (i, j) in temp:
                        return False

                    temp.add((i, j))
                    add(i - 1, j, water_lvl)
                    add(i+1, j, water_lvl)
                    add(i, j-1, water_lvl)
                    add(i, j+1, water_lvl)


        add(1, 0, res)
        add(0, 1, res)
        visited.update(temp)
        
        


        while (n, n) not in visited:
            temp.clear()

            res += 1
            for x in list(visited):
                i = x[0]
                j = x[1]
                add(i - 1, j, res)
                add(i+1, j, res)
                add(i, j-1, res)
                add(i, j+1, res)
            visited.update(temp)

        return res