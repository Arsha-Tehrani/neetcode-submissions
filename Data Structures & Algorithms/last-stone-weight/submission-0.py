class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            y = stones[-1]
            x = stones[-2]
            if x == y:
                stones.pop()
                stones.pop()

            elif x < y:
                stones.pop()
                stones.pop()
                new = y-x
                stones.append(new)
                stones.sort()

        if len(stones) == 1:
            return stones[0]

        return 0
        


