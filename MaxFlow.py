class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph 
        self.ROW = len(graph) 

    def BFS(self,s, t, parent): 
  
        visited =[False]*(self.ROW) 
          
        queue=[] 
          
        queue.append(s) 
        visited[s] = True

        while queue: 
  
            v = queue.pop(0) 
          
            for ind, val in enumerate(self.graph[v]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = v 

        return True if visited[t] else False           
      
    def Dinic(self, source, sink): 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 
  
        while self.BFS(source, sink, parent) : 

            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            max_flow +=  path_flow 
  
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 

if __name__ == "__main__":
    graph = [[0, 16, 13, 0, 0, 0], 
            [0, 0, 10, 12, 0, 0], 
            [0, 4, 0, 0, 14, 0], 
            [0, 0, 9, 0, 0, 20], 
            [0, 0, 0, 7, 0, 4], 
            [0, 0, 0, 0, 0, 0]] 
    g = Graph(graph)
    print(g.Dinic(0,len(graph)-1))