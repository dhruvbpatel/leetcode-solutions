class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return [i**2 for i in sorted(A,key=lambda x:x**2)]