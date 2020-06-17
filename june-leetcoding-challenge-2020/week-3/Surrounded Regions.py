class Solution:
    def dfs(self,i,j):
            if i>=0 and i<len(self.board) and j>=0 and j<len(self.board[0]) and self.board[i][j]=='O':
                self.board[i][j]='S'
                self.dfs(i+1,j)
                self.dfs(i-1,j)
                self.dfs(i,j+1)
                self.dfs(i,j-1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board



        rlen = len(board)

        if rlen <=2:
            return 
        
        clen = len(board[0])
        
        if clen<=2:
            return

        

        for i in range(rlen):
            for j in range(clen):
                if board[i][j]=='O' and (i==0 or j==0 or i==rlen-1 or j==clen-1): ## only for border O apply dfs and update connected O
                    self.dfs(i,j)
                    ##  now all not surrounded zeros are changed to 'S'

                    ## now at last chaneg O to x and S to O 
        for i in range(rlen):
            for j in range(clen):
                if self.board[i][j]=='O':self.board[i][j]='X'
                elif self.board[i][j]=='S':self.board[i][j]='O'


