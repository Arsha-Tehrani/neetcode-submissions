class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def back(array, remain, pos):
            if remain == 0:
                res.append(list(array))
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]:
                    continue

                elif remain - candidates[i] < 0:
                    break

                n = candidates[i]
                array.append(n)
                back(array, remain - n, i+1)
                array.pop()

        back([], target, 0)

        return res