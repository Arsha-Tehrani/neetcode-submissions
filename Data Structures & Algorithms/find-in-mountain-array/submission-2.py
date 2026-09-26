class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #Find Peak Index
        left = 0
        right = mountainArr.length() - 1
        found = False
        res = 100000
        while left < right and not found:
            m = (left + right) // 2
            m_r = m + 1
            m_l = m - 1

            cur = mountainArr.get(m)
            l = mountainArr.get(m-1)
            r = mountainArr.get(m + 1)
            if cur > l and cur > r:
                peak = m
                found = True

            if cur > l:
                left = m + 1
            else:
                right = m
        
        #Search left side
        left = 0
        right = peak
        while left < right:
            m = (left + right) // 2
            cur = mountainArr.get(m)
            if target == cur:
                res = min(res, m)
                right = m
                return res

            #Binary
            if target < cur:
                right = m
                continue
            else:
                left = m + 1
                continue

        if mountainArr.get(left) == target:
            return left

        #Check right of peak
        left = peak
        right = mountainArr.length() - 1
        while left < right:
            m = (left + right) // 2
            cur = mountainArr.get(m)
            if target == cur:
                res = min(res, m)
                right = m
                return res

            #Binary
            if target < cur:
                left = m + 1
                continue
            else:
                right = m 
                continue

        if mountainArr.get(left) == target:
            return left
        
        return -1