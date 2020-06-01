class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack =[]
        n=k
        
        for i in num:
            while n and stack and stack[-1]>i:
                stack.pop()
                n-=1
            stack.append(i)
        # print(stack)
        ans = "".join(stack[0:len(num)-k])
        ans=ans.lstrip('0')
        # print(ans)
        if len(ans)>0:
            return ans
        else:
            return "0"
        
            
                
        