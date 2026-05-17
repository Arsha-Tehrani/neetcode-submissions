class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_set = defaultdict(int)
        freq_test = defaultdict(int)
        left = 0
        cur_length = 10000
        window = [0] * 2
        found = False

        for i in t:
            freq_set[i] += 1
        #print(freq_set)
        for i in range(len(s)):
            if freq_set[s[i]] > 0:
                left = i
                for j in range(left, len(s)):
                    freq_test[s[j]] += 1
                    if all(freq_test.get(k, 0) >= v for k, v in freq_set.items()):
                        found = True
                        #print(freq_test)
                        #print(j, left)
                        #print(cur_length)
                        if (j - left + 1) < cur_length:
                            window[0] = left
                            window[1] = j
                            cur_length = j-left+1
                        break

                

                freq_test.clear()
                


        if found:
            return s[window[0]:window[1] + 1]
        else:
            return ""
