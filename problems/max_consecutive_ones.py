class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr=0
        count=0
        
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
            
            if nums[i]==0 or i==len(nums)-1:
                if curr>=count:
                    count=curr
                curr=0
                
        return count