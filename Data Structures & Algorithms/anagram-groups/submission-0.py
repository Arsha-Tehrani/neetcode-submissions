class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for i in strs:
            if sorted(i) not in anagrams:
                anagrams.append(sorted(i))

        #print(len(anagrams))
        final = [[] for _ in range(len(anagrams))]
        
        
        for j in strs:
            sorted_j=sorted(j)
            for k in range(len(anagrams)):
                if sorted_j == anagrams[k]:
                    #print(f"sorted_j = {sorted_j}")
                    #print(f"k = {k}")
                    #print(j)
                    final[k].append(j)
                    #print(final)
                

        return final