class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        d = {0:-1}  ## initilaiza a dict 
        count = 0
        max_subarr = 0
        
        
        for i in range(len(nums)):
            if nums[i]==0:  ## +1 for i and -1 for 0
                count-=1
            else:
                count+=1
            
            if count in d:   ## if the count is in d 
                curr = i-d[count]   ## find current max by  index-value of d[count]
                if curr>max_subarr: ## update the max 
                    max_subarr=curr
            else:  ## if count not in dict
                d[count]=i ## add it


        return max_subarr  ## at the end return max_subarr
                
        
        
        
                    
                
                
        
        
        
            
            
            
        
            
            
        
        
        
        
        
        