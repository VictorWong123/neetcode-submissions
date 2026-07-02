class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in arr:
            diff = abs(x-i)
            heapq.heappush(heap,(diff,i))
        res = []
        for i in range(k):
            diff, x = heapq.heappop(heap)
            res.append(x)
        res.sort()
        return res