class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        arr = sorted(costs,key=lambda x:abs(x[0]-x[1]),reverse=True)
        
        print(arr)
        total = 0
        
        a_count = 0
        b_count = 0
        
        n=len(arr)
        
        for i in range(len(arr)):
            
            if a_count!=n//2 and b_count!=n//2:
                if arr[i][0]>arr[i][1]:
                    curr=arr[i][1]
                    total+=curr
                    b_count+=1
                    continue
                else:
                    curr=arr[i][0]
                    total+=curr
                    a_count+=1
                    continue
                    
            if b_count==n//2 and a_count!=n//2:
                curr=arr[i][0]
                total+=curr
                a_count+=1
                continue
            if a_count==n//2 and b_count!=n//2:
                curr=arr[i][1]
                total+=curr
                b_count+=1
                continue
                
                
        return total
            
                
            
            
            
                
            
            
        