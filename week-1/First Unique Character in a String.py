class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={i:0 for i in s}

        print(d)
        for i in s:
            d[i]+=1
        print(d)
        count =0
        for i in s:
            
            if(d[i]==1):
                return count
            count+=1
        return -1
        

# sol=Solution()   
# print(sol.firstUniqChar("loveleetcode"))

# from collections import Counter
# s="loveleetcode"
# d=Counter(s)
# print(d)

# for i,c in enumerate(s):
#     if d[c]==1:
#         print(i)
#         break
# print(-1)
