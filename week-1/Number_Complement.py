import math as mt
class Solution:
    def findComplement(self, num: int) -> int:
        if num ==0:
            return 1
        bit_len = int(mt.log2(num))+1
        x = int(mt.pow(2,bit_len))-1
        
        return num^x
        
        