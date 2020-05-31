class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_arr = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                
                if i==0:
                    dp_arr[0][j]=j
                elif j==0:
                    dp_arr[i][0]=i
                    
                elif word1[i-1] == word2[j-1]:  # if word char is same,copy diagonal
                    dp_arr[i][j]=dp_arr[i-1][j-1]
                else:  # else 1+min of left ,up,diagonal
                    dp_arr[i][j]=1+min(dp_arr[i-1][j-1],dp_arr[i-1][j],dp_arr[i][j-1])
        return dp_arr[i][j] # return last element
        
