class Solution:
    
    def kadane(self,A):
        
        sum_till_now = A[0]
        max_sum=A[0]
        
        for i in A[1:]:
            sum_till_now = max(i,sum_till_now+i)
            max_sum = max(max_sum,sum_till_now)
        return max_sum
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        kadane_sum = self.kadane(A)

        circular_sum = 0

        for i in range(len(A)):
            circular_sum+=A[i]
            A[i]*=-1


        circular_sum_kadane = self.kadane(A)

        circular_sum +=circular_sum_kadane

        #print(kadane_sum, " " ,circular_sum)
        
        if circular_sum>kadane_sum and circular_sum!=0:
            return circular_sum
        else:
            return kadane_sum
            
            


        
        
            
        
        
        