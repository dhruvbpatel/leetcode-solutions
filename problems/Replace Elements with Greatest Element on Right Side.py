class Solution
    def replaceElements(self, arr List[int]) - List[int]
        
        
        ### so far best approach 
        
        n = len(arr)
        maxSoFar = arr[n-1]
        arr[n-1]=-1
        
        for i in range(n-2,-1,-1)
            if arr[i]maxSoFar
                arr[i],maxSoFar=maxSoFar,arr[i]
            else
                arr[i]=maxSoFar
        return arr
                
        ## approach 2
        
#         maxSoFar = -1
        
#         for i in range(len(arr)-1,-1,-1)
#             temp = arr[i]
#             arr[i]=maxSoFar   ## in 1st iteration replace last element with -1
            
#             if temp  maxSoFar
#                 maxSoFar = temp
#         return arr
        
        
        
        ## inefficient approach
#         for i in range(len(arr))
#             if i=len(arr)-2
#                 arr[i]=max(arr[i+1])
            
                
#         arr[-1]=-1
        
#         return arr
        
    
        