class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        fin = []
        res = 0
        track = set()
        for i in range(len(s)):
            res += 1
            cur = s[i]
            track.add(cur)
            count[cur] -= 1

            if count[cur] == 0:
                track.remove(cur)

            if len(track) == 0:
                fin.append(res)
                res = 0

        return fin

            