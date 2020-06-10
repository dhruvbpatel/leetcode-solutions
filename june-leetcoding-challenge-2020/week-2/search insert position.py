class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## approach -2 :optimized using binary search
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left

    ### approach -1 simple linear search
#         count =0
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 return i
#             if nums[i]<target:
#                 count+=1
#         return count
        
            
            
            
        