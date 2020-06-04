class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        #[4,3,2,1,1]
        
        1) for 4th ind and make neg , i.e make 1 neg ==> -1
        same for all
        
        
        at the end ans=5
        '''
        
        
        ## aproach -2 
        ans =[]
        
        for i in nums:  
            ind = abs(i)-1    ## store the corresponding index of element value
            if nums[ind]>0: ## go to that index and make negative if not
                nums[ind]*=-1
                
        for i in range(len(nums)):  ## now iterate
            if nums[i]>0: ## if num is positive
                ans.append(i+1) ## add the index in pos
        
        return ans
            
        
        
        
        
        
        
        