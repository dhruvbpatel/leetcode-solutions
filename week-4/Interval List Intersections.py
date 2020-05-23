class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        i =0
        j=0
        ans = []
        
        while i<len(A) and j<len(B):
            
            low = max(A[i][0],B[j][0])  ## find lower limit
            high = min(A[i][1],B[j][1])  ## find upper limit
            
            if low<=high:  
                ans.append([low,high])
            
            if A[i][1]<B[j][1]:  ## now check if max of A is smaller than max of B
                i+=1  ## if yes then only increase i 
            else:
                j+=1  ## else increase j 

        return ans




### another approach 

#         ans = []
        
#         i=0
#         j=0
        
#         while i<len(A) and j<len(B):
            
#             a_min =A[i][0]
#             a_max =A[i][1]
            
#             b_min = B[j][0]
#             b_max = B[j][1]
            
            
#             if a_max<b_min:  # if a_max is smaller than b_min,means a is out of range in B
#                 i+=1 
#             elif b_max<a_min:  # same way here B is out of range of A
#                 j+=1
            
#             else:
                
#                 if a_max<b_max: ## they are in range but a_max is small than b_max
                    
#                     i+=1
#                 else:
#                     j+=1
                    
#                 ans.append([max(a_min,b_min),min(a_max,b_max)])
#         return ans
                        
                        
                    
            
        