## approach -1

# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums = sorted(set(nums))
        
#         if len(nums)<3:
#             return nums[-1]
#         else:
#             return nums[-3]


## approach 2
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums) # remove all duplicates
        x=max(nums) ## find max
        if len(nums)>2:  ## if len >2
            for i in range(2): ## loop for only 2 times as to find 3rd max
                nums.remove(x) ## now array will be one size less
                if len(nums)!=0:  ## if our array is not empty 
                    x=max(nums)  ##update x =max(nums), 2nd and 3rd max will be updated at the end
                else:
                    break ## if len =0 break 
        return x # return our x
 