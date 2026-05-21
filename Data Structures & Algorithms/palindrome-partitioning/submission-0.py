class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_pall(word):
            i = 0 
            j = len(word)-1

            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1

            if len(word) > 0:
                return True
            else:
                return False

        def dfs(i, cur):
            # Base Case: If our slice index reaches the end of the string, 
            # it means every chunk we collected was a valid palindrome.
            if i >= len(s):
                res.append(cur.copy())
                return
            
            # Try every possible end position (j) for the current slice
            for j in range(i, len(s)):
                # Extract the chunk from index i up to j
                slice_str = s[i:j+1]
                
                # The Filter you realized you needed!
                if is_pall(slice_str):
                    cur.append(slice_str)  # Add the valid chunk
                    dfs(j + 1, cur)        # Recurse on the REMAINING part of the string
                    cur.pop()              # Backtrack to try a different slice length

        # Start the recursion at index 0 with an empty list
        dfs(0, [])
        
        return res