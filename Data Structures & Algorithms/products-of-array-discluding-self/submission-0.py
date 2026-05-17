class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix product
        prefix = 1
        pre = []
        n= len(nums) 
        for i in range(n):
            pre.append(prefix)
            prefix *= nums[i]

        #suffix product
        suffix = 1
        suf = []
        for j in range(n-1, -1, -1):
            suf.append(suffix)
            suffix *= nums[j]

        
        final = []
        for x in range(n):
            final.append(pre[x] * suf[n-1-x])

        return final