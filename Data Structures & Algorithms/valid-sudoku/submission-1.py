class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        sq_sets = [set() for i in range(9)] 
        
        for i in range(9):

            row_set = set()
            col_set = set()

            for j in range(9):
                # check rows and squares
                if board[i][j] != ".":
                    num = int(board[i][j])
                    index = int(i/3) * 3 + int(j/3)
                    
                    if num in row_set or num in sq_sets[index]:
                        return False
                    
                    sq_sets[index].add(num)
                    row_set.add(num)
                # check cols
                if board[j][i] != ".":
                    num = int(board[j][i])
                    
                    if num in col_set:
                        return False

                    col_set.add(num)
        
        return True

        