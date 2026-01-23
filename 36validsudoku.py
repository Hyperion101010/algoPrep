class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mp = []
        for i in range(9):
            tmp = [0 for _ in range(11)]
            row_mp.append(tmp)
        
        col_mp = []
        for i in range(9):
            tmp = [0 for _ in range(11)]
            col_mp.append(tmp)
        
        # This counts occurence in each row and column.
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                else:
                    nm = int(board[r][c])
                    row_mp[r][nm] += 1
                    col_mp[c][nm] += 1

        # This checks for duplicates in each row and column.
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != '.':
                    nm = int(board[r][c])
                    if row_mp[r][nm] + col_mp[c][nm] > 2:
                        return False

        # To test if the 3 by 3 matrix is valid.
        # First maintain a lookup for each matrix.
        # Then in each matrix check on the count and if there is more 
        # than one occurence then its invalid.
        for r in range(3):
            r_c = r*3
            for c in range(3):
                c_c = c*3
                lkup = [0 for _ in range(10)]
                for each_r in range(r_c, r_c + 3):
                    for each_c in range(c_c, c_c + 3):
                        if board[each_r][each_c] != '.':
                            nm = int(board[each_r][each_c])
                            lkup[nm] +=1
                            if lkup[nm] > 1:
                                return False

        return True
