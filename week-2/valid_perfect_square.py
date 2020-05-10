class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ## using binary search
        
        start = 1
        end = num
        
        if num==1:
            return True
        
        
        while start<end:
            mid = (start+end)//2
            if mid**2 > num:
                end = mid
            elif mid**2<num:
                start = mid+1
            else:
                return True
        return False
                
        