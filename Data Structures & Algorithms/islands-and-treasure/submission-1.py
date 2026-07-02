class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append((row,col))
                    seen.add((row,col))

        def bfs(row,col):
            if row<0 or row>rows-1 or col<0 or col>cols-1 or (row,col) in seen or grid[row][col]== -1:
                return

            seen.add((row,col))
            q.append((row,col))

        dist= 0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = dist
                bfs(row+1,col)
                bfs(row-1,col)
                bfs(row,col+1)
                bfs(row,col-1)

            dist +=1

