class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sl = len(s)
        tl = len(t)
        
        sp =0  ## s pointer
        tp=0   ## t pointer
        
        while sp<sl and tp<tl:  ### realized no need for list just iterate over str
            if s[sp]==t[tp]:
                sp+=1
            tp+=1
            
        return sp==sl
        
        
        
        ## my approach - 1 
#         if s=="" and t=="":
#             return True
        
#         if t=="":
#             return False
        
#         if s=="":
#             return True
        
#         sl = list(s)
#         tl = list(t)
        
        
        
#         sp=0
        
        
#         stack = []
        
#         for i in t:
#             if sp==len(sl):
#                 return True
            
#             if i==sl[sp]:
#                 stack.append(sl[sp])
#                 sp+=1
                
#         if sp==len(sl):
#             return True
            
            
            
        
        
        