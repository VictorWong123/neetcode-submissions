class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        out = [(-v,i) for i,v in hashmap.items()]
        heapq.heapify(out)
        res = []

        for i in range(k):
            x,y =heapq.heappop(out)
            res.append(y)

        return res