class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set=set(J)
        count=0
        for i in S:
            if i in j_set:
                count+=1
        return count
        