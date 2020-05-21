
# # The isBadVersion API is already defined for you.
# # @param version, an integer
# # @return a bool
# # def isBadVersion(version):

# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         start =1
#         end = n
        
#         if isBadVersion(start):  ## if the first element itself is True
#             return start
        
#         while start<end:   ## using BinarySearch Approach
#             mid =(start+end)//2
            
#             if(isBadVersion(mid)==True) and (mid==0 or isBadVersion(mid-1)==False):
#                 return mid
            
#             elif isBadVersion(mid)==True:
#                 end=mid
#             else:
#                 start=mid+1
#         return start


## another approach

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n-1
        
        while start<=end:
            mid = (start+end)//2  ## finding mid
            if isBadVersion(mid):  ## checki if mid is Bad --> if true
                if(isBadVersion(mid-1)): # also if mid is True and mid-1 is also true then search mid-1
                    end=mid-1
                else: ### if mid-1 is false then our mid is first number
                    return mid
            else:
                start = mid+1  ##search in right side
                
        return start  ## if loop ends return start
        
        

