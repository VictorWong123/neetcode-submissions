class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        rows = len(heights)
        cols = len(heights[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col ==0:
                    pacific.add((row,col))
                if row == rows-1 or col == cols-1:
                    atlantic.add((row,col))
        
        def bfs(start):
            visited = set(start)
            q = deque(start)
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c = row+dr, col+dc

                    if (0<=r<rows and 0<=c<cols and (r,c) not in visited and heights[r][c]>=heights[row][col]):
                        visited.add((r,c))
                        q.append((r,c))
                    
            return visited
        x = bfs(atlantic)
        y = bfs(pacific)
        return list(x & y)



        