class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        targ = total // k
        nums.sort()
        sides = [0] * k

        def back(index):
            nonlocal sides
            nonlocal targ
            if index == len(nums):
                return True

            for i in range(k):
                if sides[i] + nums[index] <= targ:
                    sides[i] += nums[index]

                    if back(index + 1):
                        return True

                    sides[i] -= nums[index]

                    if sides[i] == 0:
                        break
            
            return False


        return back(0)
        