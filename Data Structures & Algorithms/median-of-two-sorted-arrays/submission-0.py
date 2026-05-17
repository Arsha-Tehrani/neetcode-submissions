class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        r = 0
        n1 = len(nums1)
        n2 = len(nums2)
        res = []


        while l < n1 and r < n2:
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1

        res.extend(nums1[l:])
        res.extend(nums2[r:])
        m = len(res) // 2
        if len(res) % 2 == 0:
            return (res[m]+res[m-1])/2
        else:
            return res[int(m)] 