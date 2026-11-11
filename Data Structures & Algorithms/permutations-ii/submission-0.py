class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #You start with each entry number of UNIQUES - 1 times
        count = Counter(nums)
        res = []
        temp = []
        def back():
            nonlocal res
            nonlocal temp
            if len(temp) == len(nums):
                res.append(temp.copy())
                return

            for i in count:
                if count[i] > 0:
                    temp.append(i)
                    count[i] -= 1
                    back()
                    temp.pop()
                    count[i] += 1

        back()
        return res