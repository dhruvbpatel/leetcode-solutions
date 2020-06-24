from math import factorial
class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n)//(factorial(n)*factorial(n)*(n+1))


s = Solution()
n=5
print(s.numTrees(n))