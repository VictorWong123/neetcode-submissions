class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                    visited.add((row,col))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0 
        while q:
            n = len(q)
            for i in range(n):
                row,col = q.popleft()
                for dx,dy in directions:
                    r,c = row+dx, col + dy
                    if 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 1 and (r,c) not in visited:
                        grid[r][c] = 2
                        q.append((r,c))
                        visited.add((r,c))
            if q:
                res +=1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return res

