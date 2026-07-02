class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        seen = set()

        def addRoom(row,col):
            if row>=rows or row<0 or col>=cols or col<0 or (row,col) in seen or grid[row][col]==-1:
                return
            q.append([row,col])
            seen.add((row,col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append([row,col])
                    seen.add((row,col))
        dist = 0 
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = dist

                addRoom(row+1,col)
                addRoom(row-1,col)
                addRoom(row,col+1)
                addRoom(row,col-1)
            dist+=1