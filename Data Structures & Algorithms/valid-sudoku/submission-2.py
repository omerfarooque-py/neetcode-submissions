class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        collumns = set()
        grids = set()
        for r in range(9):
          for c in range(9):
            val = board[r][c]
            if val == ".":
              continue
            if (r, val) in rows: return False
            rows.add((r, val))    
            if (c, val) in collumns: return False
            collumns.add((c, val))        
            box = (r//3 , c//3)
            if (box, val) in grids: return False
            grids.add((box, val))

        return True