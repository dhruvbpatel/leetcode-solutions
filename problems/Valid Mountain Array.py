class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3:
            return False
        
        slope = "incr"
        
        
        for i in range(1,len(arr)):
            if i==1:
                if arr[i]>arr[i-1]:
                    continue
                else:
                    return False
            
            if slope=='incr':
                if arr[i]>arr[i-1]:
                    pass
                    
                elif arr[i]==arr[i-1]:
                    return False
                else:
                    slope='dec'
                    continue
                    
            if slope=='dec':
                if arr[i]<arr[i-1]:
                    continue
                else:
                    return False
                
            if i==len(arr)-1 and slope=='incr':
                return False
            
                
                
            
        return True        
            
            
## editorial 
'''
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
'''
