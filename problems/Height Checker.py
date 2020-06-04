class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs=sorted(heights)
        count =0
        for i in range(len(heights)):
            if heights[i]!=hs[i]:
                count+=1
        return count
                
        
        
        