class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        visited = set()

        def backtrack(row, col, k):
            if len(path) == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            if word[k] == board[row][col] and (row, col) not in visited:
                path.append(board[row][col])
                visited.add((row, col))
                if backtrack(row+1, col, k+1) or backtrack(row-1, col, k+1) or backtrack(row, col+1, k+1) or backtrack(row, col-1, k+1):
                    return True
                path.pop()
                visited.remove((row, col))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(i,j,0):
                    return True
        return False
            