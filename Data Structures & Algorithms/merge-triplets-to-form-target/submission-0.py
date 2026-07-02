class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        sett = set()
        for x,y,z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:  
                if x == target[0]:
                    sett.add(0)
                if y == target[1]:
                    sett.add(1)
                if z == target[2]:
                    sett.add(2)

                if len(sett)==3:
                    return True
        

        return False