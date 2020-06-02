class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        hashset=set()
        
        for i in arr:
            if i*2 in hashset:
                return True
            if i%2==0:
                if i/2 in hashset:
                    return True
            hashset.add(i)
        return False
        