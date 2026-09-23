class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(big):
            i = 0
            cur = 0
            temp = 1
            while i < len(weights):
                if cur + weights[i] <= big:
                    cur += weights[i]
                    i += 1
                    continue
                else:
                    cur = 0
                    temp += 1

            if temp <= days:
                return True
            
            else:
                return False

        
        small = max(weights)
        big = sum(weights)

        while small < big:
            m = (small + big) // 2
            if check(m) == True:
                big = m
                continue
            else:
                small = m + 1

        return small