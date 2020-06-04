class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #return sorted(A,key=lambda x:x%2==0,reverse=True)

        ## using quick sort approach

        i =0
        j = len(A)-1
        
        while i<j:
            if A[i]%2>A[j]%2:  # if A[i]%2==1 (means odd) and A[j]%2==0 (means even) , swap them 
                A[i],A[j]=A[j],A[i]
            
            if A[i]%2==0:i+=1 # else incr i as i is in correct position 
            if A[j]%2==1:j-=1 # else decr j as j is in correct position 
        return A