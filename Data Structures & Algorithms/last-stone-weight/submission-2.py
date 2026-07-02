class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x<y:
                heapq.heappush(stones, -(y-x))
        if stones:
            return -stones[0]
        return 0 