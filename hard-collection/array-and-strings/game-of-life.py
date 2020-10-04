class Solution(object):
    def gameOfLife(self, board):
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                neighbours = 0
                if i > 0 and j > 0:
                    neighbours += (board[i-1][j-1] % 10)
                if i > 0:
                    neighbours += (board[i-1][j] % 10)
                if i > 0 and j < m - 1:
                    neighbours += (board[i-1][j+1] % 10)
                if j > 0:
                    neighbours += (board[i][j-1] % 10)
                if j < m - 1:
                    neighbours += (board[i][j+1] % 10)
                if i < n - 1 and j > 0:
                    neighbours += (board[i+1][j-1] % 10)
                if i < n - 1:
                    neighbours += (board[i+1][j] % 10)
                if i < n - 1 and j < m - 1:
                    neighbours += (board[i+1][j+1] % 10)
                
                if board[i][j] == 1:
                    if neighbours < 2 or neighbours > 3:
                        board[i][j] = board[i][j] + 20
                    else:
                        board[i][j] = board[i][j] + 30
                else:
                    if neighbours == 3:
                        board[i][j] = board[i][j] + 30
                    else:
                        board[i][j] = board[i][j] + 20
        
        for i in range(n):
            for j in range(m):
                if board[i][j] // 10 == 2:
                    board[i][j] = 0
                elif board[i][j] // 10 == 3:
                    board[i][j] = 1
        
        return board