class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stack = []
        trips.sort(key=lambda x: x[2])
        curr = 0

        for i in trips:
            passengers, start, to = i
            curr += passengers
            while stack and stack[-1][2] <= start:
                p, f, t = stack.pop()
                curr -= p
            
            stack.append(i)
            if curr> capacity:
                return False
            

        return True
