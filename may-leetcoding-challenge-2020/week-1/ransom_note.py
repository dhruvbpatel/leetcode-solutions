# class Solution:

#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d ={i:0 for i in magazine}
        
#         for i in magazine:
#             d[i]+=1
#         for j in ransomNote:
#             if(j not in d):
#                 return False
#             elif (d[j]>0):
#                 d[j]-=1
#             else:
#                 return False
#         return True

## my new solution

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = Counter(magazine)
        
        for i in ransomNote:
            if magazine_dict[i]>0: ## if magazine_dict has i 
                magazine_dict[i]-=1  ## decrease count by 1
            else:
                return False  ## if not then we can't construct ransom from magazine , return false
        return True  ## if everything is fine , return True