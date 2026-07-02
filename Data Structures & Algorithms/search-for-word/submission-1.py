class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c,i,sett):
            print(i)
            if i == len(word):
                return True

            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c] != word[i] or (r,c) in sett:
                return False

            sett.add((r,c))    
            found = (dfs(r+1,c,i+1,sett) or dfs(r-1,c,i+1,sett)or dfs(r,c+1,i+1,sett) or dfs(r,c-1,i+1,sett))
            sett.remove((r,c))

            return found


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0,set()):
                        return True
        return False
                
