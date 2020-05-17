from collections import  Counter

class Solution:
    def findAnagrams(self, s,p):
        
        slen = len(s)
        plen = len(p)
        
        if slen<plen:
            return []
        ans = []
        ## creating a dict with freq
        s_dict = Counter()
        p_dict = Counter(p)
        
        for i in range(slen):
            s_dict[s[i]]+=1
            
            if i>=plen:   ## when we have traversed length greater than plen
                if s_dict[s[i-plen]]==1:  ## now if our s[i-plen] is also in s_dict with freq 1 means our dict is having size more than plen, so we can remove i-plen element
                	# print(i,end=" ")

                	# print(s_dict,end=" ")
                	# print(s_dict[i],end=" ")
                	# print(s_dict[plen])
                	# print(s[i-plen])

                	# # print("1: s_dict[s[i-plen]]","i:",i,"i-plen:",i-plen,s_dict[s[i-plen]])
                	del s_dict[s[i-plen]]  ## delete
                	pass
                else:
                	# print(i,end=" ")
                	# print(s_dict)
                	# print("2:","i:",i,"i-plen:",i-plen,s_dict[s[i-plen]])

                	s_dict[s[i-plen]]-=1 ## if dict element is having freq more than 2
            if p_dict == s_dict:
                ans.append(i-plen+1)
        return ans
                    
            

# s= Solution()
# print(s.findAnagrams("ababend","ab"))        
        
        
        
        
        
