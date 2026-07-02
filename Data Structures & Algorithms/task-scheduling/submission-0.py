class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        max_heap = [-i for i in counter.values()]

        q= deque()
        time = 0 

        while max_heap or q:
            time +=1
            if max_heap:
                x = heapq.heappop(max_heap) +1

                if x:
                    q.append([x,time+n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(max_heap,q.popleft()[0])

        return time