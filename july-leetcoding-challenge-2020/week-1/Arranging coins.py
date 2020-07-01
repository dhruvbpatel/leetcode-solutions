class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        total = n
        i=1
        while total>=0:
            if total-i>=0:
                total-=i
                count+=1
            else:
                break
            i+=1
        return count
## editorial approach

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         left, right = 0, n
#         while left <= right:
#             k = (right + left) // 2
#             curr = k * (k + 1) // 2
#             if curr == n:
#                 return k
#             if n < curr:
#                 right = k - 1
#             else:
#                 left = k + 1
#         return right
            
            
            
            
            
        