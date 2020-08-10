class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self, A, row, col, vis):
        vis[row][col] = True

        Row = [0, 1, 0, -1]
        Col = [1, 0, -1, 0]

        for r, c in zip(Row, Col):
            new_r = row + r
            new_c = col + c

            if self.isValid(A, new_r, new_c) and not vis[new_r][new_c] and A[new_r][new_c] == 'O':
                self.dfs(A, new_r, new_c, vis)

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]


        for i in range(m):
            if A[i][0] == 'O':
                self.dfs(A, i, 0, vis)

            if A[i][n - 1] == 'O':
                self.dfs(A, i, n - 1, vis)

        for j in range(n):
            if A[0][j] == 'O':
                self.dfs(A, 0, j, vis)

            if A[m - 1][j] == 'O':
                self.dfs(A, m - 1, j, vis)

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    A[i][j] = 'X'

        return A

    def bfs(self, A):
        m = len(A)
        n = len(A[0])
        q = []
        vis = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if A[i][j] == 'O':
                        A[i][j] = 'B'
                    vis[i][j] = True

                elif i == m - 1 or j == n - 1:
                    if A[i][j] == 'O':
                        A[i][j] = 'B'

                    vis[i][j] = True

        while q:
            i, j = q.pop(0)
            vis[i][j] = True
            row = [0, 1, 0, -1]
            col = [1, 0, -1, 0]

            for r, c in zip(row, col):
                new_r = i + r
                new_c = j + c

                if new_r < 0 or new_r > m - 1 or new_c < 0 or new_c > n - 1 and vis[new_r][new_c]:
                    continue
                vis[new_r][new_c] = True

                if A[new_r][new_c] == 'O':
                    A[new_r][new_c] = 'X'

        return A


if __name__ == '__main__':
    A = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]

    C = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]

    B = Solution()
    print(B.solve(C))
