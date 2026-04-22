class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      collumns = set()
      rows = set()
      boxes = set()
      for r in range(9):
        for c in range(9):
          val = board[r][c]
          box = (r//3, c//3)
          if val == ".":
            continue 
          print(c, val)
          if (r, val) in rows or (c, val) in collumns or (box, val) in boxes:
            return False
          rows.add((r,val))
          collumns.add((c,val))
          boxes.add((box, val)) 
      return True 
            