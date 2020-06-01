## approach 1
## approach using dictionaries in python O(logn) time and O(n) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d={}
        
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        #print(d)
        for k,v in d.items():
            if d[k]==1:
                return k
        
        return 

# approach 2

# from functools import reduce
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         return reduce(lambda x,y : x^y , nums)  ## this will xor over all elements and give the single element in the lis
        
    
            
### approach 3:
## binary seach  O(logn) time and O(1) space

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left =0
        right = len(nums)-1

        while left<right:

            mid = (left+right)//2

            check_subarray_even = (right-mid)%2==0 
             ## checking if our both left and right halves are odd or even


            if nums[mid]==nums[mid+1]: ### if our same element of mid is right side
                if check_subarray_even: ## and our halves are even
                    left=mid+2  ## move left to mid+2
                else:
                    right = mid-1 ## our halves are odd , so move right to mid-1

            elif nums[mid]==nums[mid-1]: ## our same element is in left side
                if check_subarray_even: ## our halves are even
                    right =mid-2  #move right to mid-2
                else:
                    left=mid+1  ## halves are odd, move left to mid+1
            else:
                return nums[mid]  ## if mid is single element return 

        return nums[right]  ## continue till left==right and return that element
        ## in case of [1,1,2]  ## at the end left==right so return nums[right]