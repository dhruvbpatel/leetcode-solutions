  class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(num+1):
            
            dp[i]=dp[i>>1] + int(i&1)  ## i>>1 == i//2 
        
        return dp
            
        

            
