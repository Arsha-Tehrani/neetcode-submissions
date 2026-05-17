class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Upper bound for answer = largest element in array
        upper = 0

        for i in piles:
            upper = max(upper, i)

        r = upper
        l = 1

        while l <= r:
            m = l + int((r-l)/2)
            time_taken = 0
            for i in piles:
                time_taken += (i + m - 1) // m 
            
            if time_taken <= h:
                res = m
                r = m-1
            else:
                l = m+1

        
        return res

        