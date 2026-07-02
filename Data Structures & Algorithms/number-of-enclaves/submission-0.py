class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if (row ==0 or row==ROWS-1 or col==0 or col==COLS-1) and grid[row][col]==1:
                    q.append((row,col))
                    grid[row][col]=-1

        while q:
            row,col = q.popleft()
            for dx,dy in direction:
                r,c = row+dx, col+dy
                if 0<=r<ROWS and 0<=c<COLS and grid[r][c] ==1:
                    q.append((r,c))
                    grid[r][c] = -1
        res = 0    
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] ==1:
                    res +=1
        return res