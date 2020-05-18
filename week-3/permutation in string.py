from collections import  Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        s2_counter = Counter()
        s1_counter = Counter(s1)
        

        for i,char in enumerate(s2):
            
            s2_counter[char]+=1

            if i>=len(s1):
                rem_ele = s2[i-len(s1)]

                if s2_counter[rem_ele]==1:
                    del s2_counter[rem_ele]
                else:
                    s2_counter[rem_ele]-=1
            if s1_counter==s2_counter:
                return True
        return False

# s= Solution()

# ans = s.checkInclusion("a","ab")
# print(ans)