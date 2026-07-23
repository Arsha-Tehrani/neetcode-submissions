class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
         #Iterate, find a target, set that as my focus
         #Check if the found numbers are more than each one if any of the remaining matched.

        cur = 0
        at = -1
        bt = -1
        ct = -1
        for i in range(len(triplets)):
            end = False
            a = triplets[i][0]
            b = triplets[i][1]
            c = triplets[i][2]

            if a == target[0]:
                at = target[0]
                cur = i
                end = True

            if b == target[1]:
                bt = target[1]
                cur = i
                end = True

            if c == target[2]:
                ct = target[2]
                cur = i
                end = True
            
            if end:
                break

        print(at,bt,ct, cur)
        for j in range(i+1, len(triplets)):
            a = triplets[j][0]
            b = triplets[j][1]
            c = triplets[j][2]

            if at > 0 and bt > 0 and ct > 0:
                return True

            if at > 0 and at < a:
                continue
            
            if bt > 0 and bt < b:
                continue

            if ct > 0 and ct < c:
                continue

            if at < 0 and a == target[0]:
                at = a
            if bt < 0 and b == target[1]:
                bt = b
            if ct < 0 and c == target[2]:
                ct = c

        if at > 0 and bt > 0 and ct > 0:
                return True
        
        return False
                    
            

            



