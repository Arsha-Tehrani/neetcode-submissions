class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        done = set()
        res = []
        for i in nums:
            if i not in counter: counter[i] = 1
            else: counter[i] += 1
            if counter[i] > (len(nums)/3) and i not in done:
                res.append(i)  
                done.add(i)

        return res