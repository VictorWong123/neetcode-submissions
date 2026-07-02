class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hashmap = Counter(hand)

        for i in hand:
            if hashmap[i]==0:
                continue

            for j in range(i,i+groupSize):
                if hashmap[j]==0:
                    return False
                hashmap[j]-=1

        return True