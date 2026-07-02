class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        
        res.append(intervals[0])
        for interval in intervals: 
            if interval[0]<= res[-1][0] and interval[1] >= res[-1][0]:
                x,y = res.pop()
                res.append([min(x,interval[0]),max(y,interval[1])])

            elif interval[0]>= res[-1][0]and interval[0]<=res[-1][1]:
                x,y = res.pop()
                res.append([min(x,interval[0]),max(y,interval[1])])
            elif res[-1][1] == interval[0]:
                x,y = res.pop()
                res.append([x,interval[1]])
            else:
                res.append(interval)

        return res
