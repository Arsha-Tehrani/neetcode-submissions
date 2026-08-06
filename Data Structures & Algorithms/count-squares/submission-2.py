from typing import List

class CountSquares:

    def __init__(self):
        # Store points and their frequencies
        self.db = {}

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        # Increment the count of this specific point
        self.db[p] = self.db.get(p, 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        
        # Iterate through every point in the database to see if it can form a diagonal
        for (nx, ny), count in self.db.items():
            
            # 1. To be a diagonal of a square, the x-distance must equal the y-distance.
            # 2. Distance must be > 0 (area cannot be 0, so nx cannot equal qx).
            if abs(nx - qx) == abs(ny - qy) and nx != qx:
                
                # If (nx, ny) is the opposite diagonal to (qx, qy), 
                # the other two corners MUST be at (nx, qy) and (qx, ny).
                corner1 = (nx, qy)
                corner2 = (qx, ny)
                
                # Check if both of these required corners exist in our database
                if corner1 in self.db and corner2 in self.db:
                    # The number of ways to form this square is the product of the 
                    # frequencies of the 3 points already in the database.
                    res += count * self.db[corner1] * self.db[corner2]
                    
        return res