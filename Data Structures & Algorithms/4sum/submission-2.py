class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        #print(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = n - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    #print([nums[i], nums[j], nums[left], nums[right]])
                    if temp == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        #print(res)
                        left += 1
                        right -= 1
                    
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    
                    elif temp > target:
                        right -= 1
                    
                    elif temp < target:
                        left += 1
        
        return res