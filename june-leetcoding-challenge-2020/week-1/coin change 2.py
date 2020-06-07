class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        dp[0][0]=1
        
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j-coins[i-1]>=0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
                    
        