
from collections import  Counter
class Solution:
    def frequencySort(self, s: str) -> str:
    	sc = Counter(s)

    	sc_sorted=sorted(sc,key=lambda x:sc[x],reverse=True)
    	#print(sc_sorted)
    	ans=''
    	#print(sc_sorted)
    	for i in sc_sorted:
    		ans+=i*sc[i]
    	return ans

    	

## another approach , this is quite fast beats 99% sol


# from collections import  Counter
# class Solution:
#     def frequencySort(self, s: str) -> str:
#     	ans = "".join(char*freq for char,freq in Counter(s).most_common())
#     	#print(ans)
#     	return ans


    	
 
