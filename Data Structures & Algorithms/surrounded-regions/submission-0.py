class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def bfs(row,col):
            q = deque()
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            q.append((row,col))


            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    board[row][col]= "E"


                    for dx,dy in direction:
                        r,c = row+dx, col+dy
                        if 0<=r<rows and 0<=c<cols and board[r][c] =="O":
                            q.append((r,c))

        for row in range(rows):
            for col in range(cols):
                if (row==0 or row ==rows-1 or col==0 or col==cols-1) and board[row][col]=="O":
                    bfs(row,col)


        for row in range(rows):
            for col in range(cols):
                if board[row][col]=="O":
                    board[row][col] = "X"
                if board[row][col] =="E":
                    board[row][col] = "O"
