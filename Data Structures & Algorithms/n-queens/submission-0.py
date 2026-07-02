class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        pos_d = set()
        neg_d = set()
        cols = set()
        

        def dfs(i,sol):
            if i ==n:
                res.append(build_board(sol))
                return
            for col in range(n):
                if col in cols or (col+i) in pos_d or (i-col) in neg_d:
                    continue

                cols.add(col)
                pos_d.add(col+i)
                neg_d.add(i-col)
                sol.append(col)
                dfs(i+1,sol)
                
                cols.remove(col)
                pos_d.remove(col+i)
                neg_d.remove(i-col)
                sol.pop()

        def build_board(sol):
            board = []
            for col in sol:
                row = ["."] * n
                row[col] = "Q"
                board.append("".join(row))
            return board

            


            


            


        dfs(0,[])
        return res
