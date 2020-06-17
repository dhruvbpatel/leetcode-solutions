class Solution:
    def getRow(self, r: int) -> List[int]:
        m = [[0]*(i+1) for i in range(r+1)]
        
        
        for i in range(r+1):
            for j in range(len(m[i])):
                if j==0 or j==i:
                    m[i][j]=1
                else:
                    m[i][j]=m[i-1][j-1]+m[i-1][j]
        return m[-1]
                        
                    
        