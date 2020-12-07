from flask_socketio import emit
import time
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph 
        self. ROW = len(graph) 

    def BFS(self,s, t, parent): 
  
        visited =[False]*(self.ROW) 
          
        queue=[] 
          
        queue.append(s) 
        visited[s] = True
           
        while queue: 
  
            u = queue.pop(0) 
          
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        if visited[t] :
            v = t
            path = str(t)
            while(v !=  s):
                v = parent[v]
                path = path +"<-"+ str(v)
            emit("new message",{'message' : 'Chọn đường đi: {}'.format(path),'tag':"new message"})
            time.sleep(0.3)
            return True  
        else:
            return False
              
      
    def FordFulkerson(self, source, sink): 
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