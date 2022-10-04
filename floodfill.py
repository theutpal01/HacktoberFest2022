"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
"""
class Solution:
    def dfs(self, image, sr, sc, source, color):
        rows = len(image)
        columns = len(image[0])
        if(sr <0 or sc >=columns or sc<0 or sr>=rows):
           return 
        elif image[sr][sc]!=source:
           return
        else:
           image[sr][sc]= color
           self.dfs(image, sr-1, sc, source, color)
           self.dfs(image, sr+1, sc, source, color)
           self.dfs(image, sr, sc-1, source, color)
           self.dfs(image, sr, sc+1, source, color)
           return image
        
         
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if color == image[sr][sc]:
            return image
        source = image[sr][sc]
        self.dfs(image, sr, sc, source,color)
        return image
    
    