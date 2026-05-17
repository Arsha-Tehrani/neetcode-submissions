class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        uniq = sorted(set(nums))
        n = len(uniq)
        count = 1
        result = 0
        print(uniq)
        for i in range(n-1):
            if uniq[i+1] - uniq[i] == 1:
                count += 1
            else:
                if count > result:
                    result = count
                
                count = 1
        
        if count > result:
            result = count
        
        return result
