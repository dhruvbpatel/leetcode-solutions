
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start =1
        end = n
        
        if isBadVersion(start):  ## if the first element itself is True
            return start
        
        while start<end:   ## using BinarySearch Approach
            mid =(start+end)//2
            
            if(isBadVersion(mid)==True) and (mid==0 or isBadVersion(mid-1)==False):
                return mid
            
            elif isBadVersion(mid)==True:
                end=mid
            else:
                start=mid+1
        return start



