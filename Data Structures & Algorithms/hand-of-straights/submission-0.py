class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        i = len(hand) - 1
        count = 0
        while i >= 0:
            print(hand)
            if count == groupSize:
                count = 0
                i = len(hand)-1
            
            if count == 0:
                temp = hand.pop(i)
                count += 1
                i -= 1

            else:
                if temp - hand[i] == 1:
                    temp = hand.pop(i)
                    i -= 1
                    count += 1
                elif temp - hand[i] == 0:
                    i -= 1

                else:
                    return False

        return len(hand) == 0