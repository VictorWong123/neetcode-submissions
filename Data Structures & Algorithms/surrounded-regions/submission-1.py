class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q= deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row==0 or col == 0 or row==ROWS-1 or col==COLS-1) and board[row][col]=="O":
                    q.append((row,col))
                    board[row][col] = "Y"
        
        while q:
            row,col = q.popleft()
            for dx,dy in directions:
                r,c = row+dx, col+dy
                if 0<=r<ROWS and 0<=c<COLS and board[r][c] =="O":
                    board[r][c] = "Y"
                    q.append((r,c))
        
        for row in range(ROWS): 
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "Y":
                    board[row][col] = "O"
