class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_set = defaultdict(int)
        freq_check = defaultdict(int)
        n = len(s1) 
        left = 0

        for i in s1:
            freq_set[i] += 1

        for right in range(len(s2)):
            freq_check[s2[right]] += 1
            while freq_check[s2[right]] > freq_set[s2[right]]:
                freq_check[s2[left]] -= 1
                left += 1
            

            if freq_check == freq_set:
                return True

        return False