class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N==1:
            return 1
        
        
        score_list = [0]*(N+1)
        
        #print(score_list)
        
        for s1,s2 in trust:
            
            
            score_list[s1]-=1
            
            score_list[s2]+=1
            
        #print(score_list)
        
        
        for i in range(1,N+1):
            
            if score_list[i]==N-1:
                return i
            
            
        return -1
        
        
        
            
            
        
            
            
        
       
        