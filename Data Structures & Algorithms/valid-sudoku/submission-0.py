class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Go through the entire sudoku board and look for one invalid section
        # if one singular section is invalid, return false
        seen = set()
        isValid = True
        i = 0
        j = 0

        while i < 9:
            while j < 9:
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] in seen:
                            return False
                        elif board[k][l] != ".":
                            seen.add(board[k][l])
                j += 3
                seen.clear()
            i += 3

        seen.clear()
        # Then, check each row
        for i in range(9):
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != ".":
                    seen.add(board[i][j])
            seen.clear()

        seen.clear()
        # Then, check each column
        for i in range(9):
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != ".":
                    seen.add(board[j][i])
            seen.clear()
    
        # If you make it to the end, return true
        return True