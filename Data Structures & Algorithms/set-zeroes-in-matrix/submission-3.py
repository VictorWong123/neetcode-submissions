class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        cols = set()
        rows = set()

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(i)
                    rows.add(j)

        for i in range(m):
            for j in range(n):
                if i in cols or j in rows:
                    matrix[i][j] = 0
