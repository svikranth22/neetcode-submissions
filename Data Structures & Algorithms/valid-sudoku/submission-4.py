class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        sq_sets = [set() for i in range(9)] 
        
        for i in range(9):

            row_set = set()
            col_set = set()

            for j in range(9):
                # check rows and squares
                if board[i][j] != ".":
                    index = (i//3) * 3 + (j//3)
                    
                    if (board[i][j] in row_set
                        or board[i][j] in sq_sets[index]):
                        return False
                    
                    sq_sets[index].add(board[i][j])
                    row_set.add(board[i][j])
                # check cols
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False

                    col_set.add(board[j][i])
        
        return True

        