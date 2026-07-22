class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num] == 0:
                continue
            
            for i in range(num, num + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1

        return True