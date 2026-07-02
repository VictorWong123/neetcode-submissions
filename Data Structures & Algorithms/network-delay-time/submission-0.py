class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for i in times:
            s = i[0]
            t = i[1]
            w = i[2]

            adj_list[s].append([t,w])

        minHeap = [[0,k]]
        shortest = {}

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj_list[n1]:
                if n2 in shortest:
                    continue 
                heapq.heappush(minHeap, [w1+w2,n2])

        if len(shortest)<n:
            return -1

        return max(shortest.values())