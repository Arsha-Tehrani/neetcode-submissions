class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Tuple up capital and profit
        #Sort by capital needed
        #add possible profits to a Heap

        mixed = []
        for i in range(len(profits)):
            pair = (capital[i], -profits[i])
            mixed.append(pair)

        mixed.sort(key = lambda x : x[0])
        
        actions = []
        heapq.heapify(actions)
        res = []
        track = 0
        while len(res) < k:
            while track < len(mixed):
                if mixed[track][0] <= w:
                    heapq.heappush(actions, mixed[track][1])
                    track += 1
                else: break
            
            if len(actions) < 1:
                break
            best = heapq.heappop(actions)
            res.append(best)
            w -= best

        return w