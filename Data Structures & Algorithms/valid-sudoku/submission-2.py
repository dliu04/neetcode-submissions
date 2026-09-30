class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # key: (r // 3, c // 3)

        # Of a particular row, keep track of a value. If the same value occurs in the same row, return False.
        # Of a particular column, keep track of a value. If the same value occurs in the same column, return False.
        # Of a particular 3 by 3 box, keep track of a value. If the same value occurs in the same box, return False.

        # Square is a little tricky in particular because of how it is indexed. We don't want to track each entry,
        # so we divide by three to split it into three subsquares. Then, store values into the subsquare and check for
        # duplicates within them.

        # The key will be a tuple since sets cannot be interacted with like lists. However, we can use two indices to identify
        # a particular square by using a tuple type as the key.
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        
        return True
