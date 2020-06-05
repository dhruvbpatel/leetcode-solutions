class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = []  ## cummulative sum array
        cs = 0
        
        for i in w:
            cs+=i
            self.cum_sum.append(cs)
        print(self.cum_sum)
        self.sum = cs
        
        

    def pickIndex(self) -> int:
        randn = random.random() * self.sum
        ## using binary search 
        print(randn)
        return bisect.bisect_left(self.cum_sum, randn)  ## using bisect which internally uses binary search only

    ## or implementing binary search
    
#         low =0
#         high = len(self.cum_sum)
        
#         while low<high:
#             mid = (low+high)//2
            
#             if randn > self.cum_sum[mid]:
#                 low = mid+1
#             else:
#                 high = mid
#         return low
            
                
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()