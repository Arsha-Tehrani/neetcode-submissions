class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        cur = 0
        res = []
        for i in range(len(arr)):
            if arr[i] < x:
                continue
            
            else:
                starting = i
                break

        l = i-1
        while cur < k:
            if l > -1: left = arr[l]
            else: left = float("inf")
            if i < len(arr): right = arr[i]
            else: right = float("inf")
            if abs(left-x) <= abs(right-x):
                res.append(left)
                l -= 1
                cur += 1
            else:
                res.append(right)
                i += 1
                cur += 1
        res.sort()
        return res