class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for i in strs:
            sorted_i = sorted(i)
            if sorted_i not in anagrams:
                anagrams.append(sorted_i)
        final = [[] for _ in range(len(anagrams))]     
        
        for j in strs:
            sorted_j=sorted(j)
            for k in range(len(anagrams)):
                if sorted_j == anagrams[k]:
                    final[k].append(j)
                

        return final