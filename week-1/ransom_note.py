class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d ={i:0 for i in magazine}
        
        for i in magazine:
            d[i]+=1
        for j in ransomNote:
            if(j not in d):
                return False
            elif (d[j]>0):
                d[j]-=1
            else:
                return False
        return True