class Solution:
    def validIPAddress(self, IP: str) -> str:
        v4_candidate = IP.split('.')
        if len(v4_candidate) == 4 and self.isIPV4Address(v4_candidate):
            return "IPv4"
        
        v6_candidate = IP.split(':')
        if len(v6_candidate) == 8 and self.isIPV6Address(v6_candidate):
            return "IPv6"
        
        return "Neither"
    
    def isIPV4Address(self, lists):
        for x in lists:
            if not x.isdigit():
                return False
            if x[0] == '0' and len(x) > 1:
                return False
            x_digit = int(x)
            #print(x_digit)
            if x_digit < 0 or x_digit > 255:
                #print("False")
                return False
        return True
    
    def isIPV6Address(self, lists):
        for x in lists:
            if len(x) > 4 or len(x) == 0:
                return False
            for letter in x:
                letter_int = ord(letter)
                if not (
                    (letter_int >= ord('0') and letter_int <= ord('9')) or
                    (letter_int >= ord('a') and letter_int <= ord('f')) or
                    (letter_int >= ord('A') and letter_int <= ord('F'))):
                    return False
        return True
    
    ## editorial solution using regex
    
#     import re
# class Solution:
#     chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
#     patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
#     chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
#     patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

#     def validIPAddress(self, IP: str) -> str:        
#         if self.patten_IPv4.match(IP):
#             return "IPv4"
#         return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 