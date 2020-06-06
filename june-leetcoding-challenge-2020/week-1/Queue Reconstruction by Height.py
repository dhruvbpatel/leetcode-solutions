class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))## sort accrdn to desc order height and comparing x[1] if x[0] is same
        print(people)
        ans=[]
        
        for i in people:
            ans.insert(i[1],i)  ## now insert the sublist i at i[1] index 
            
        return ans
        