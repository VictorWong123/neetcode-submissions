class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #diff, i
        max_heap = []
        for i, (a,b) in enumerate(costs):
            diff = abs(a-b) 
            heapq.heappush(max_heap,(-diff,i))
        
        A = 0
        B = 0
        n = len(costs)/2
        res = 0 

        while A<n and B<n:
            diff, idx = heapq.heappop(max_heap)
            diff *= -1
            if costs[idx][0]<costs[idx][1]:
                res += costs[idx][0]
                A+=1
            else:
                res += costs[idx][1]
                B+=1

        while A<n:
            diff, idx = heapq.heappop(max_heap)
            diff *=-1
            res += costs[idx][0]
            A+=1
        
        while B<n:
            diff, idx = heapq.heappop(max_heap)
            diff *=-1
            res += costs[idx][1]
            B+=1
        return res