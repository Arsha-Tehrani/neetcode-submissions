class Solution:
    def reorganizeString(self, s: str) -> str:
        #ord(a) == 97
        #ord(z) == 122
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1

        most_freq = max(count)
        most = chr(count.index(most_freq) + 97)
        count[count.index(most_freq)] = 0

        if most_freq > ((len(s)-1) // 2) + 1:
            return ""

        res = ["*"] * len(s)
        ind = 0
        for _ in range(most_freq):
            res[ind] = most
            ind += 2
        
        stock = []
        for i in range(len(count)):
            if chr(i + 97) == most:
                continue
            stock = stock + [chr(i + 97)] * count[i]

        for i in range(26):
            while count[i] > 0:
                # If we reach the end, wrap around to start filling odd indices
                if ind >= len(s):
                    ind = 1
                    
                res[ind] = chr(i + 97)
                ind += 2
                count[i] -= 1

        return "".join(res)