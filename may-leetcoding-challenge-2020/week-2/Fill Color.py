class Solution:
    
    
    def helper(self,image,sr,sc,newColor,currColor):
        if sr>=len(image) or sc>=len(image[sr]):
            return
        if sr<0 or sc<0:
            return
        
        if image[sr][sc]==newColor or image[sr][sc]!=currColor:
            return 
        
        image[sr][sc]=newColor
        
        self.helper(image,sr-1,sc,newColor,currColor)
        self.helper(image,sr+1,sc,newColor,currColor)
        self.helper(image,sr,sc-1,newColor,currColor)
        self.helper(image,sr,sc+1,newColor,currColor)
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.helper(image,sr,sc,newColor,image[sr][sc])
        return image
    
        