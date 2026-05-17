class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        vis = defaultdict(int)
        for x in range(n):
            for y in range(x+1, n, 1):
                for z in range(y+1, n, 1):
                    summ = nums[y] + nums[x] + nums[z]
                    temp = [nums[x], nums[y], nums[z]]
                    temp.sort()
                    if (summ == 0) and (vis[tuple(temp)] != 1):
                        #print(nums[x],nums[y],nums[z])
                        #print(vis[temp.sort()])
                        res.append([nums[x], nums[y], nums[z]])
                        vis[tuple(temp)] = 1

        return res