class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        
        for fast in range(len(nums)):
            if nums[fast]!=0:  ## if slow and fast are at same position swap will not change place , only when 0 comes fast will move forward and replace will change array
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        
                
            
        
#         for fast in range(len(nums)):
#             if nums[slow]==0:
#                 if nums[fast]!=0:
#                     nums[slow],nums[fast]=nums[fast],nums[slow]
#                     slow+=1
#             else:
#                 slow+=1
#         print(nums)

                
            
            	
        
        