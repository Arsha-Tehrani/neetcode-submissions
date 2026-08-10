class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = 0
        upper = float("-inf")
        zero = False

        for i in nums:
            if i == 0:
                zero = True
            cur += i
            upper = max(upper, i)


        for i in range(upper + 1):
            cur -= i
                
        if cur == 0 and zero:
            return upper + 1
        
        return -cur