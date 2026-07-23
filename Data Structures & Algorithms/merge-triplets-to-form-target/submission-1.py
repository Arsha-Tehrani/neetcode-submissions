class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Track if we have found the target numbers in our "safe" triplets
        found_a = found_b = found_c = False
        
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
                
            if a == target[0]: found_a = True
            if b == target[1]: found_b = True
            if c == target[2]: found_c = True
            
        return found_a and found_b and found_c