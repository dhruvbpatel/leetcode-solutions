# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         j_set=set(J)
#         count=0
#         for i in S:
#             if i in j_set:
#                 count+=1
#         return count
#         

## my new solution

from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s_dict = Counter(S)
        
        total_count =0
        
        for i in J:
            total_count +=s_dict[i]
        return total_count
