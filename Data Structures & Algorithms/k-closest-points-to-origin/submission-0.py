class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(i[0]**2 + i[1]**2), i] for i in points]

        heapq.heapify(points)
        res = []

        while k>0:
            x=heapq.heappop(points)
            res.append(x[1])
            k-=1

        return res
