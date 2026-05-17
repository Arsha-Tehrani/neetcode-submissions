class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0

        while i < j:
            
            cur = (j-i) * min(heights[i], heights[j])
            res = max(res, cur)
            #print(i,j, res)

            if heights[i] <= heights[j]:
                i += 1
            
            else:
                j-= 1

        return res
