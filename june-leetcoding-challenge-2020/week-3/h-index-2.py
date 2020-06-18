class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        start = 0
        end = l-1
        
        while start<=end:
            mid = (start+end)//2
            
            if citations[mid]==l-mid:
                return citations[mid]
            elif citations[mid]>l-mid:
                end = mid-1
            else:
                start = mid+1
        
        return l-start
        
### editorial

        # start =0 
        # end= n-1
        # l=len(citations)
        # while start<=end:
        #     mid =(start+end)//2

        #     if citations[mid]>=l-mid:
        #         end=mid-1
        #     else:
        #         start=mid+1
        # return l-end




        