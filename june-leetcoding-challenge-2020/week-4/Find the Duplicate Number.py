from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## approach-2  O(nlogn) ans O(1) space
        nums.sort()
        slow = 0
        
        for fast in range(1,len(nums)):
            
            if nums[slow]!=nums[fast]:
                slow+=1
                continue
            else:
                break
        return nums[slow]

## editorial
# class Solution:V
#     def findDuplicate(self, nums):
#         # Find the intersection point of the two runners.
#         tortoise = hare = nums[0]
#         while True:
#             tortoise = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break
        
#         # Find the "entrance" to the cycle.
#         tortoise = nums[0]
#         while tortoise != hare:
#             tortoise = nums[tortoise]
#             hare = nums[hare]
        
#         return hare
        
        ## approach - 1 using O(n) space and O(n) complexity
#         d = Counter(nums)
        
        
#         for ind,val in enumerate(d):
#             if d[val]>=2:
#                 return val
        
        
        
        