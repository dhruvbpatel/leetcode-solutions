class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:


    	total = 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        new_mat = [[0]*(col+1) for i in range(row+1)]  ## create a new matrix of size n+1 * m+1
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                
                if matrix[i-1][j-1]==1:  ## only if the value in matrix is 1
                    new_mat[i][j]=1+min(new_mat[i-1][j],new_mat[i][j-1],new_mat[i-1][j-1]) ## find min and add 1
                
                    total+= new_mat[i][j]  ## sum 

        return total

 ## approach 2:

        # total = 0
        
        # for i in range(1,len(matrix)):   ## traverse in matrix
        #     for j in range(1,len(matrix[0])): 
        #         if matrix[i][j]==1: 
        #             matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1 ## update the matrix itself with min+1
        
        # return sum(map(sum,matrix))  ## return the sum of the matrix which is the ans

 

                    
                    
                
            
            
        