class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        nums.sort()  ## sort all elements for we get proper order only
        
        ans = [[i] for i in nums]   ## make ans like  [[1],[2],[3]]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(ans[i])<len(ans[j])+1:   ## eg: if 2%1==0 and  len([2])<len([1])+1 , because we may get  len([2,1])<len([3]) , for which we need not to add 
                    ans[i]=ans[j]+[nums[i]]  ## add  [1]+[2]=[2,1]
                    
        return max(ans,key=len)     ## return max according to key=len 
        
        
        
        