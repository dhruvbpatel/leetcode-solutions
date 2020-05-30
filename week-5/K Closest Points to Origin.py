class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         dist_arr = [((i[0]**2+i[1]**2)**(1/2),i) for i in points]
#         dist_arr.sort(key=lambda x:x[0])
#         return [j[1] for i,j in enumerate(dist_arr)][:K]
        
        
        
        
        # approach 1
        
        dist_arr =[]
        ind_arr =[]
        
        for i,j in enumerate(points):
            dist = (j[0]-0)**2 + (j[1]-0)**2
            dist = dist**(1/2)
            
            ans=[j,dist]
            
            dist_arr.append(ans)
        
        dist_arr.sort(key=lambda x:x[1])
        
        ans =[ ]
        for i in range(K):
            ans.append(dist_arr[i][0])
        return ans


''' 
editorial approach

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
'''
            
