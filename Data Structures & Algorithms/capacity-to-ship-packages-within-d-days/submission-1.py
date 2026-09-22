from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if a given capacity can ship everything within 'days'
        def can_ship(capacity: int) -> bool:
            days_needed = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight > capacity:
                    # Ship is full, ship it and start a new day
                    days_needed += 1
                    current_weight = weight
                else:
                    # Add to the current day's shipment
                    current_weight += weight
                    
            return days_needed <= days

        # The search space for our capacity
        left = max(weights)  # Minimum possible capacity (must hold the heaviest item)
        right = sum(weights) # Maximum possible capacity (holds everything in 1 day)
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                # If we can ship it, try to find a smaller valid capacity
                right = mid
            else:
                # If we can't, we absolutely need a larger capacity
                left = mid + 1
                
        return left