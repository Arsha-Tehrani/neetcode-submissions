class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        final = []
        for j in range(k):
            val = 0
            most = 0
            for key in count:
                if count[key] > val:
                    val = count[key]
                    most = key
            
            final.append(most)
            count[most] = 0

        return final
                