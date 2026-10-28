import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Only add characters to the heap if their count is > 0
        heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count < 0:
                heapq.heappush(heap, (count, char))
                
        res = []
        
        while heap:
            count1, char1 = heapq.heappop(heap)
            
            # Check if appending the most frequent character violates the rule
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                # If there is no second character to fall back on, we must stop
                if not heap:
                    break
                
                # Pop the second most frequent character instead
                count2, char2 = heapq.heappop(heap)
                res.append(char2)
                count2 += 1 # Decrement magnitude
                
                # Push the second character back if it still has remaining count
                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))
                    
                # Push the first character back unused
                heapq.heappush(heap, (count1, char1))
                
            else:
                # Safe to append the most frequent character
                res.append(char1)
                count1 += 1
                
                if count1 < 0:
                    heapq.heappush(heap, (count1, char1))
                    
        return "".join(res)