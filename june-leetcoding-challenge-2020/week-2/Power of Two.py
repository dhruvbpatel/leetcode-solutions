class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n==0:
            return False
        if n==1:
            return True
        
        oneless = n-1  ## eg: if n=4 , its binary representation would be 100 , so onless = 011
        
        ## now logic is to & n and oneless
        ## if result is 0 then n is a power of 2 else not
        
        if n&oneless==0:
            return True
        else:
            return False
        
        