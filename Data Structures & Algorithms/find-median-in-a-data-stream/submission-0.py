import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        heapq.heapify(self.minHeap)




    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap,num)

    def findMedian(self) -> float:
        n = len(self.minHeap)

        temp = []
        for i in range(n//2):
            x = heapq.heappop(self.minHeap)
            temp.append(x)

        print(self.minHeap[0])
        if n%2==0:
            res =  (self.minHeap[0] + x)/2

        else:
            res =  self.minHeap[0]
            
        for i in temp:
            heapq.heappush(self.minHeap,i)
        return res

        