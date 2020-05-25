class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        ## using DP approach
        
        l1 = len(A) ## row
        l2 = len(B)## col
        
        dp_arr = [[0 for i in range(l2+1)] for j in range(l1+1)]  
        
        
        
        for i in range(l1):
            for j in range(l2):
                #print(i,j)
                if A[i]==B[j]:
                    dp_arr[i+1][j+1]=dp_arr[i][j]+1
                else:
                    dp_arr[i+1][j+1]=max(dp_arr[i+1][j],dp_arr[i][j+1])
                    
        
        return dp_arr[l1][l2]
