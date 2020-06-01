
class Solution:
    def checkStraightLine(self, coordinates):
        slope_y =coordinates[1][1]-coordinates[0][1]
        slope_x= coordinates[1][0]-coordinates[0][0]
        if slope_x==0:
            return False
        slope = slope_y/slope_x
        
        print("slope:",slope)
        
        
        for i in range(1,len(coordinates)):
            y =coordinates[i][1]-coordinates[i-1][1]
            x=coordinates[i][0]-coordinates[i-1][0]
            
            # if x<=0:
            #     return False
            # if y==0:
            #     new_slope=0
            #     print("new_slope:",i,new_slope)
            # else:
            if x==0:
                return False
            new_slope=y/x
            # print("new_slope :",i,new_slope)
            
            if new_slope!=slope:
                return False
        return True

l=[[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]

s=Solution()
ans=s.checkStraightLine(l)
print(ans)
