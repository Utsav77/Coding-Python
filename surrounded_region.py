class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(A,x,y):
            if(x >= 0 and x < len(A) and y >= 0 and y < len(A[0]) and A[x][y] == 'O'):
                A[x][y] = 'P'
                dfs(A, x + 1, y)
                dfs(A, x, y + 1)
                dfs(A, x - 1, y)
                dfs(A, x, y - 1)
            else:
                return
        
        m = len(A)
        if(m == 0):
            return
        n = len(A[0])
        for i in range(m):
            if(A[i][0] == 'O'):
                dfs(A, i, 0)
        
        for i in range(m):
            if(A[i][n-1] == 'O'):
                dfs(A, i, n-1)

        for j in range(n):
            if(A[0][j] == 'O'):
                dfs(A, 0, j)

        for j in range(n):
            if(A[m - 1][j] == 'O'):
                dfs(A, m - 1, j)

        
        for i in range(m):
            for j in range(n):
                if(A[i][j] == 'O'):
                    A[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if(A[i][j] == 'P'):
                    A[i][j] = 'O'
    