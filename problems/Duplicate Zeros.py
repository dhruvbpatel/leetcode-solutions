class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # [1,0,2,3,0,4,5,0]
        
        
        l=len(arr)
        
        new_arr =[]
        i=0
        
        for i in range(len(arr)+1):
            if(len(new_arr)>=l):
                break;
            new_arr.append(arr[i])
            
            if(len(new_arr)>=l):
                break;
            if arr[i]==0:
                new_arr.append(0)
        # print(arr)
        # print(new_arr)
        for j in range(len(new_arr)):
            arr[j]=new_arr[j]
    
            
        