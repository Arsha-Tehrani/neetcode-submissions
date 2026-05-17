class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            one = numbers[i]
            two = numbers[j]
            if one + two == target:
                return [i+1,j+1]

            elif one + two > target:
                j -= 1
            elif one + two < target:
                i += 1
