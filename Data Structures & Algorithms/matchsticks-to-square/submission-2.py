class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        
        # If the total length isn't divisible by 4, a square is impossible
        if total_sum % 4 != 0:
            return False
            
        target = total_sum // 4
        
        # Optimization 1: Sort in descending order. 
        # Placing the largest matchsticks first helps us fail faster if a path is invalid.
        matchsticks.sort(reverse=True)
        
        # Create 4 buckets for the 4 sides of the square
        sides = [0, 0, 0, 0]
        
        def backtrack(i):
            # Base case: If we have placed all matchsticks, we are done!
            if i == len(matchsticks):
                return True
                
            # Try placing the current matchstick into one of the 4 sides
            for j in range(4):
                # If adding this matchstick exceeds the target length, skip this side
                if sides[j] + matchsticks[i] <= target:
                    
                    # Do
                    sides[j] += matchsticks[i]
                    
                    # Recurse: If this placement leads to a solution, return True
                    if backtrack(i + 1):
                        return True
                        
                    # Undo (Backtrack)
                    sides[j] -= matchsticks[i]
                    
                # Optimization 2: If this bucket is empty and it didn't work, 
                # there's no point in trying the next empty buckets (they are identical)
                if sides[j] == 0:
                    break
                    
            return False
            
        return backtrack(0)