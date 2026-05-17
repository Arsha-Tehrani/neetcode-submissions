class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        freq = [[] for _ in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)

        final = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                final.append(n)
                if len(final) == k:
                    return final