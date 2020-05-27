
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        d = {}  ## take a dict
        
        for val in dislikes:  ## iterate over dislikes
            if val[0] in d:
                d[val[0]].add(val[1])   
            else:
                d[val[0]]=set([val[1]])
            if val[1] in d:
                d[val[1]].add(val[0])
            else:
                d[val[1]]=set([val[0]])
        
        
        visited = {}  
        
        for i in range(1,N+1):
            if i not in visited:
                visited[i]=0
                stack =[i]  ## add i to stack
                
                while stack:
                    a = stack.pop()
                    if a in d:
                        for b in d[a]:
                            if b in visited:
                                if visited[a]==visited[b]:
                                    return False
                            else:
                                visited[b]=(visited[a]+1)%2
                                stack.append(b)
        return True
                
        
        

## official editorial


# class Solution(object):
#     def possibleBipartition(self, N, dislikes):
#         graph = collections.defaultdict(list)
#         for u, v in dislikes:
#             graph[u].append(v)
#             graph[v].append(u)

#         color = {}
#         def dfs(node, c = 0):
#             if node in color:
#                 return color[node] == c
#             color[node] = c
#             return all(dfs(nei, c ^ 1) for nei in graph[node])

#         return all(dfs(node)
#                    for node in range(1, N+1)
#                    if node not in color)