class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        threshold = len(nums)//2
        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            
        for i in d:
            if d[i]>threshold:
                ans = i
                return ans
            