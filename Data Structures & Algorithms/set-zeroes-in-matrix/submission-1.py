class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])


        row_zeros = [False]* rows
        col_zeros = [False]*cols

        for row in range(rows):
            for col in range(cols):
                print(row,col)
                if matrix[row][col]==0:
                    row_zeros[row] = True
                    col_zeros[col] = True

        for row in range(rows):
            for col in range(cols):
                if row_zeros[row] or col_zeros[col]:
                    matrix[row][col] = 0 


        


                    