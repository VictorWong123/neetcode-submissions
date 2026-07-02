class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        q = deque()
        time = 0

        def bfs(row,col):

            if row<0 or col<0 or row>rows-1 or col>cols-1 or (row,col) in seen or  grid[row][col] == 0 :
                return 
            
            seen.add((row,col))
            if grid[row][col]==1:
                grid[row][col] = 2
                q.append((row,col))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                    seen.add((row,col))



        while q:

            for i in range(len(q)):
                row,col = q.popleft()

                bfs(row+1,col)
                bfs(row-1,col)
                bfs(row,col+1)
                bfs(row,col-1)
            if q:
                time+=1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1
        return time
